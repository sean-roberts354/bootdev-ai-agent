import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
try:
    api_key = os.environ.get("GEMINI_API_KEY")
except RuntimeError:
    print("Unable to load API key")

client = genai.Client(api_key=api_key)

def main():
    response: object = client.models.generate_content(
                                    model="gemini-2.5-flash",
                                    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    
    if response.usage_metadata == None:
        raise RuntimeError("Missing usage metadata; Likely failed API request")
    
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("-----------")    
    print(response.text)


if __name__ == "__main__":
    main()
