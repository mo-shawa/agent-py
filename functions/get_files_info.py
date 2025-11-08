import os
from typing import TypedDict


class ChildDetails(TypedDict):
    name: str
    size: int
    is_dir: bool


def get_files_info(working_directory, directory="."):
    try:
        working_directory_absolute_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, directory)
        full_absolute_path = os.path.abspath(full_path)

        if not full_absolute_path.startswith(working_directory_absolute_path):
            return f'Error: Cannot list "{full_absolute_path}" as it is outside the permitted working directory'

        if not os.path.isdir(full_absolute_path):
            return f'Error: "{full_absolute_path}" is not a directory'

        # direct children of the directory, both files and folders
        children = os.listdir(full_absolute_path)

        output_str = ""

        for child in children:

            child_path = os.path.join(full_absolute_path, child)

            data: ChildDetails = {
                "name": child,
                "size": os.path.getsize(child_path),
                "is_dir": os.path.isdir(child_path),
            }

            output_str += f"- {data['name']}: file_size={data['size']} bytes, is_dir={data['is_dir']}\n"

        return output_str

    except Exception as e:
        return f"Error: {str(e)}"
