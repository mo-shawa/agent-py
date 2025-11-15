import os
import subprocess

from google.genai import types

from functions.utils import validate_path_in_working_directory


def run_python_file(working_directory: str, file_path: str, args: list[str] = []):
    try:
        absolute_file_path = validate_path_in_working_directory(
            working_directory, file_path
        )

        if not os.path.exists(absolute_file_path):
            raise Exception(f'File "{file_path}" not found.')

        if not absolute_file_path.endswith(".py"):
            raise Exception(f'"{file_path}" is not a Python file.')

        try:
            result = subprocess.run(
                ["python3", absolute_file_path, *args],
                timeout=30,
                capture_output=True,
            )

            stdout = result.stdout.decode("utf-8")
            stderr = result.stderr.decode("utf-8")
            output_string = f"\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}"
            return output_string

        except subprocess.CalledProcessError as e:
            raise Exception(f"executing Python file: {e}")

    except Exception as e:
        return f"Error: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a Python file with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file, relative to the workding directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="An optional list of arguments",
            ),
        },
    ),
)
