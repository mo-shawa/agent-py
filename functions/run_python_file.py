from functions.utils import validate_path_in_working_directory
import os
import subprocess


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
