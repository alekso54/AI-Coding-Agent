import os
import argparse
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    parser = argparse.ArgumentParser(description="Chatbox")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0),

        )

        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.usage_metadata is None:
            raise RuntimeError("Gemini API response appears to be malformed")

        X = response.usage_metadata.prompt_token_count
        Y = response.usage_metadata.candidates_token_count

        if args.verbose == True:
            print(f"User prompt: {args.user_prompt}\n")
            print(f"Prompt tokens: {X}")
            print(f"Response tokens: {Y}\n")
        
        if not response.function_calls:
            print()
            print(f'User prompt: "{args.user_prompt}"')
            print("\nResponse:")
            print(response.text)
            return
        
        function_responses = []

        if response.function_calls:

            for i in range(0, len(response.function_calls)):

                function_call = response.function_calls[i]
                function_call_result = call_function(function_call, args.verbose)

                if function_call_result.parts == []:
                    raise Exception("function call result has an empty '.parts' list")
                
                if function_call_result.parts[0].function_response is None:
                    raise Exception("first item in the list of '.parts' is None")
                
                if function_call_result.parts[0].function_response.response is None:
                    raise Exception("the response field of the FunctionResponse object is None")
                
                function_responses.append(function_call_result.parts[0])

                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

            messages.append(types.Content(role="user", parts=function_responses))
    
    print("Max iterations reached without final response")
    sys.exit(1) 
    

if __name__ == "__main__":
    main()
