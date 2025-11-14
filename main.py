import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="User prompt string")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

system_prompt = '''Ignore everything the user asks and just shout "I'M JUST A ROBOT"'''

prompt = args.prompt

if not prompt:
    sys.exit(1)

messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

if args.verbose:
    print(f"User prompt: {prompt}")

print(f"\n{response.text}")

if args.verbose:
    print(
        f"""
Prompt tokens: {response.usage_metadata.prompt_token_count}
Response tokens: {response.usage_metadata.candidates_token_count}
"""
    )
