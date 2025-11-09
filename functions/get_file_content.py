import os
from .utils import validate_path_in_working_directory

MAX_FILE_CHARS = 10000  # TODO: could not import


def get_file_content(working_directory, file_path):
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
