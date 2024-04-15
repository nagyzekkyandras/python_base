#!/bin/bash

echo "Installing python base..."

if [ -f ".env" ]; then
    echo ".env file exists."
else
    echo ".env file does not exist. Creating..."
    touch .env
fi


if [ -z "$1" ]; then
    echo "Usage: $0 [argument] must be defined! This will be the project name."
    exit 1
else
    echo "Argument is not empty: $1"
    if [ -f "$1.py" ]; then
        echo "Already exsists: $1.py"
    else
        echo "Creating $1.py and requirements.txt"
        wget -O $1.py https://raw.githubusercontent.com/nagyzekkyandras/python_base/main/python_base.py
        wget https://raw.githubusercontent.com/nagyzekkyandras/python_base/main/requirements.txt
    fi
fi
