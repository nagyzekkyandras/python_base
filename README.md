For local development
```sh
pip3 install requests python-dotenv chardet
```

Sample main.py
```py
from modules.log import setting_up_logging
from modules.variables import check_variables

#
# Set up logging
#
logger = setting_up_logging()

# List of environment variables you want to check
env_vars = ["MY_VARIABLE_1",
            "MY_VARIABLE_2"]

#
# Init variables
#
variables = check_variables(env_vars)

#
# Functions
#
def main() -> None:
    logger.debug("Main is starting...")

if __name__ == '__main__':
    main()
```

Sample Dockerfile
```dockerfile
FROM python:3.14.0a3-alpine3.21

RUN mkdir /app
WORKDIR /app

COPY main.py /app/
COPY modules/ /app/modules/
COPY *.sh /app/

# python dependencies
RUN pip install requests python-dotenv chardet

ENTRYPOINT ["python", "/app/main.py"]
```