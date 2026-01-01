import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from agent.run_with_tools import run_with_tools
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from prompts import SYSTEM_PROMPT

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="User prompt string")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


prompt = args.prompt

if not prompt:
    sys.exit(1)


if args.verbose:
    print(f"User prompt: {prompt}")

messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

run_with_tools(
    client=client,
    available_functions=available_functions,
    prompt=prompt,
    system_instruction=SYSTEM_PROMPT,
    verbose=args.verbose,
)
