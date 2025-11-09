import os
from typing import TypedDict


class ChildDetails(TypedDict):
    name: str
    size: int
    is_dir: bool


def get_files_info(working_directory, directory="."):
    try:
        absolute_working_directory_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, directory)
        absolute_full_path = os.path.abspath(full_path)

        if not absolute_full_path.startswith(absolute_working_directory_path):
            return f'Error: Cannot list "{absolute_full_path}" as it is outside the permitted working directory'

        if not os.path.isdir(absolute_full_path):
            return f'Error: "{absolute_full_path}" is not a directory'

        # direct children of the directory, both files and folders
        children = os.listdir(absolute_full_path)

        output_str = ""

        for child in children:

            absolute_child_path = os.path.join(absolute_full_path, child)

            data: ChildDetails = {
                "name": child,
                "size": os.path.getsize(absolute_child_path),
                "is_dir": os.path.isdir(absolute_child_path),
            }

            output_str += f"- {data['name']}: file_size={data['size']} bytes, is_dir={data['is_dir']}\n"

        return output_str

    except Exception as e:
        return f"Error: {str(e)}"
