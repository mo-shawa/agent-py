from .utils import validate_path_in_working_directory
from google.genai import types


def write_file(working_directory: str, file_path: str, content: str):
    try:
        absolute_file_path = validate_path_in_working_directory(
            working_directory, file_path
        )

        with open(absolute_file_path, "w") as file:
            file.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {str(e)}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, relative to the workding directory. If the file doesn't exist, it will be created.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents to write to the file. If the file already exists, it will be overwritten.",
            ),
        },
    ),
)
