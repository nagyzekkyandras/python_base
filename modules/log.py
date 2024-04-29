import sys, os
import logging

def setting_up_logging() -> logging.Logger:
    '''
    Setting up logging. Default log level is debug.

    LOG_LEVEL can be NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
    
    Returns:
        Object: logger
    '''
    # Get log level from environment variable, defaulting to DEBUG
    log_level = os.environ.get('LOG_LEVEL', 'DEBUG').upper()

    # Configure logging
    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        stream=sys.stdout) # or specific file

    # Create a logger
    logger = logging.getLogger(__name__)
    return logger