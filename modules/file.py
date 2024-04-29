from modules.log import setting_up_logging

# Set up logging
logger = setting_up_logging()

def get_file_content(file_path) -> str:
    """
    Reads the entire content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file you want to read.

    Returns:
        str: The content of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If the file cannot be read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f"Error: The file '{file_path}' does not exist.")
        raise
    except IOError as e:
        logger.error(f"Error: Could not read file '{file_path}'. {e}")
        raise
