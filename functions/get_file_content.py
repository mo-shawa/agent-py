import os

from google.genai import types

from .utils import validate_path_in_working_directory

MAX_FILE_CHARS = 10000  # TODO: could not import


def get_file_content(working_directory: str, file_path: str):
    try:
        absolute_file_path = validate_path_in_working_directory(
            working_directory, file_path
        )

        if not os.path.isfile(absolute_file_path):
            raise Exception(
                f' File not found or is not a regular file: "{absolute_file_path}"'
            )

        with open(absolute_file_path) as file:
            file_content_string = file.read(MAX_FILE_CHARS)

            if len(file.read()) > 10000:
                file_content_string += (
                    f'[...File "{file_path}" truncated at 10000 characters]'
                )

            return file_content_string

    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the contents of a file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to get contents of, relative to the working directory.",
            ),
        },
    ),
)
