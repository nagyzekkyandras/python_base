from modules.base.log import setting_up_logging
from modules.base.variables import check_variables

# Set up logging
logger = setting_up_logging()

# List of environment variables you want to check
env_vars = ["USER"]
variables = check_variables(env_vars)

def main() -> None:
    logger.debug("Main is starting...")

if __name__ == "__main__":
    main()