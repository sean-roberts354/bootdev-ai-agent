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
    generated_content: object = client.models.generate_content(
                                    model="gemini-2.5-flash",
                                    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    
    print(generated_content.text)


if __name__ == "__main__":
    main()
