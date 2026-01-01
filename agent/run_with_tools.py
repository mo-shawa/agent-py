from typing import List

from google import genai
from google.genai import types

from functions.call_function import call_function


def run_with_tools(
    client: genai.Client,
    prompt: str,
    system_instruction: str,
    available_functions: types.Tool,
    verbose: bool,
    max_iterations: int = 20,
):

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    for _ in range(max_iterations):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                tools=[available_functions],
            ),
        )

        if response.candidates:
            for i in range(len(response.candidates)):
                content = response.candidates[i].content
                if isinstance(content, types.Content):
                    messages.append(content)

        results: List[types.Part] = []

        if (
            isinstance(response.function_calls, list)
            and len(response.function_calls) > 0
        ):
            for call in response.function_calls:
                function_call_result = call_function(call, verbose)

                # if it's a string, then there was an unhandled error that reached the except block
                if isinstance(function_call_result, str):
                    raise Exception(f"Error calling function: {function_call_result}")

                parts = function_call_result.parts

                if not parts:
                    raise Exception(f"{call.name}.parts is empty")

                function_response = parts[0].function_response

                if not function_response:
                    raise Exception(f"{call.name} response is empty")

                final_response = function_response.response

                if not final_response:
                    raise Exception(f"{call.name} final response is empty")

                results.append(parts[0])

                if verbose:
                    print(f"-> {final_response}")
            messages.append(types.Content(role="user", parts=results))
        else:
            print(f"\n{response.text}")
            break

        if verbose and response.usage_metadata:
            print(
                f"""
    Prompt tokens: {response.usage_metadata.prompt_token_count}
    Response tokens: {response.usage_metadata.candidates_token_count}
    """
            )
