import os
from dotenv import load_dotenv
from modules.log import setting_up_logging

# Set up logging
logger = setting_up_logging()

# Check each environment variable
def check_variables(env_vars, filename=".env") -> None:
    '''
    Checks env_vars variable which should contains all necessary environmental variable names.
    File can be set optionally, default value=".env".
    
    :return: None
    '''
    logger.debug("Checking vars starting...")
    for var in env_vars:
        value = os.getenv(var)
        if value:
            logger.debug(f"{var}: {value}") # Variable is set and not empty
        else:
            logger.error(f"{var} is not set or is empty. Trying to load .env file.")  # Variable is not set or is empty

            # Check if the .env file exists
            if os.path.exists(filename):
                logger.debug(".env file exists.")
                load_dotenv() # load variables from .env
                value = os.getenv(var) # check the variable again
                logger.debug(f"{var}: {value}")
            else:
                logger.error(".env file does not exist.")
    logger.debug("Checking vars ended.")