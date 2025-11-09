import os

MAX_FILE_CHARS = 10000


def get_file_content(working_directory, file_path):
    try:
        absolute_working_directory_path = os.path.abspath(working_directory)

        full_path = os.path.join(working_directory, file_path)
        absolute_file_path = os.path.abspath(full_path)

        if not absolute_file_path.startswith(absolute_working_directory_path):
            return f'Error: Cannot list "{absolute_file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_file_path):
            return f'Error: File not found or is not a regular file: "{absolute_file_path}"'

        with open(absolute_file_path) as file:

            file_content_string = file.read(MAX_FILE_CHARS)

            if len(file.read()) > 10000:
                file_content_string += (
                    f'[...File "{file_path}" truncated at 10000 characters]'
                )

            return file_content_string

    except Exception as e:
        return f"Error: {e}"
