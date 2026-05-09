import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

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
    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

    if response.usage_metadata is None:
        raise RuntimeError("Gemini API response appears to be malformed")

    X = response.usage_metadata.prompt_token_count
    Y = response.usage_metadata.candidates_token_count

    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}\n")
        print(f"Prompt tokens: {X}")
        print(f"Response tokens: {Y}\n")
    
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
