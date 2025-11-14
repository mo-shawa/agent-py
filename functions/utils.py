import os


def validate_path_in_working_directory(working_directory: str, path: str) -> str:
    absolute_working_directory_path = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, path)
    absolute_path = os.path.abspath(full_path)

    if not absolute_path.startswith(absolute_working_directory_path):
        raise Exception(
            f'Cannot access "{path}" as it is outside the permitted working directory'
        )

    return absolute_path
