import os
from google.genai import types
from typing import TypedDict
from .utils import validate_path_in_working_directory


class ChildDetails(TypedDict):
    name: str
    size: int
    is_dir: bool


def get_files_info(working_directory, directory="."):
    try:
        absolute_full_path = validate_path_in_working_directory(
            working_directory, directory
        )

        if not os.path.isdir(absolute_full_path):
            raise Exception(f'"{absolute_full_path}" is not a directory')

        # direct children of the directory, both files and folders
        children = os.listdir(absolute_full_path)

        output_str = ""

        for child in children:

            absolute_child_path = os.path.join(absolute_full_path, child)

            name = child
            size = os.path.getsize(absolute_child_path)
            is_dir = os.path.isdir(absolute_child_path)

            output_str += f"- {name}: file_size={size} bytes, is_dir={is_dir}\n"

        return output_str

    except Exception as e:
        return f"Error: {str(e)}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            )
        },
    ),
)
