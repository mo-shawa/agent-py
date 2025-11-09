from .utils import validate_path_in_working_directory


def write_file(working_directory, file_path, content):
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
