from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file


def call_function(function_call: types.FunctionCall, verbose: bool = False):
    try:
        if verbose:
            print(f"Calling function: {function_call.name}({function_call.args})")
        else:
            print(f" - Calling function: {function_call.name}")

        function_map = {
            "get_file_content": get_file_content,
            "get_files_info": get_files_info,
            "run_python_file": run_python_file,
            "write_file": write_file,
        }

        if not isinstance(function_call.name, str):
            raise Exception("Function name is not a string")

        function_to_call = function_map.get(function_call.name)

        if not function_to_call:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call.name,
                        response={"error": f"Unknown function: {function_call.name}"},
                    )
                ],
            )

        args = dict(function_call.args or {})

        args["working_directory"] = "./calculator"

        function_result = function_to_call(**args)

        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": function_result},
                )
            ],
        )

    except Exception as e:
        return f"Error: {str(e)}"
