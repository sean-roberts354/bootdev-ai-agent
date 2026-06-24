import os
import argparse
from dotenv import load_dotenv
from google import genai

def main() -> None:
    load_dotenv()
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
    except RuntimeError:
        print("Unable to load API key")

    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    response: object = client.models.generate_content(
                                    model="gemini-2.5-flash",
                                    contents=args.user_prompt)
    
    if response.usage_metadata is None:
        raise RuntimeError("Missing usage metadata; Likely failed API request")
    
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("-----------")    
    print(response.text)


if __name__ == "__main__":
    main()
