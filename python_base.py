import sys, os
import logging
from dotenv import load_dotenv

#
# Logging setup
#

# Get log level from environment variable, defaulting to DEBUG
log_level = os.environ.get('LOG_LEVEL', 'DEBUG').upper()

# Configure logging
logging.basicConfig(level=log_level,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    stream=sys.stdout) # or specific file

# Create a logger
logger = logging.getLogger()
logger.debug(f'Logging started.')

#
# Check variables
#

# List of environment variables you want to check
env_vars = ['HOME', 'PATH', 'SHELL', 'NONEXISTENT']

# Check each environment variable
def check_variables() -> None:
    '''
    Checks env_vars variable which should contains all necessary environmental variable names.
    
    :return: None
    '''
    for var in env_vars:
        value = os.getenv(var)
        if value:
            logger.debug(f"{var}: {value}") # Variable is set and not empty
        else:
            logger.error(f"{var} is not set or is empty. Trying to load .env file.")  # Variable is not set or is empty

            # Get the directory of the current script
            script_dir = os.path.dirname(__file__)

            # Path to the .env file relative to the script
            env_file_path = os.path.join(script_dir, '.env')

            # Check if the .env file exists
            if os.path.exists(env_file_path):
                logger.debug(".env file exists.")
                load_dotenv() # load variables from .env
                value = os.getenv(var) # check the variable again
                logger.debug(f"{var}: {value}")
            else:
                logger.error(".env file does not exist.")

def main() -> None:
    logger.debug("Main function running...")
    check_variables()

main()