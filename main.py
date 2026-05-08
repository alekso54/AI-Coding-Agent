import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    model = "gemini-2.5-flash"
    contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(model=model, contents=contents)

    if response.usage_metadata is None:
        raise RuntimeError("Gemini API response appears to be malformed")

    X = response.usage_metadata.prompt_token_count
    Y = response.usage_metadata.candidates_token_count

    print(f"User prompt: {contents}\n")
    print(f"Prompt tokens: {X}")
    print(f"Response tokens: {Y}\n")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
