from datetime import datetime

def get_current_datetime_formatted() -> str:
    """
    Returns the current date and time formatted as 'YYYY-MM-DD HH:MM'.

    Returns:
        str: The current datetime in the specified format.
    """
    # Get the current datetime
    current_datetime = datetime.now()
    # Format the datetime
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_datetime
