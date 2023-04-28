#!/bin/bash

# Copy the setup.service file to the systemd system folder
# sudo cp /boot/setup.service /etc/systemd/system/setup.service

sudo systemctl enable /boot/api-setup.service


# Configuration variables
CUSTOM_USERNAME="onyx"
CUSTOM_PASSWORD="opal"

CUSTOM_HOSTNAME="onyx"

GITHUB_USERNAME="jp-quant"
GITHUB_REPO="pi-api"

PROJECT_PARENT_DIR="/home/${CUSTOM_USERNAME}"
PROJECT_NAME="my_api"

FLASK_APP="app.py"

# Derived variables
PROJECT_DIR="${PROJECT_PARENT_DIR}/${PROJECT_NAME}"

# Update Raspberry Pi OS
sudo apt update
sudo apt upgrade -y

# Install required packages
sudo apt install -y git python3 python3-pip
# Check if the project directory exists
if [ -d "${PROJECT_DIR}" ]; then
    # If it exists, go to the project directory and update the repository
    cd "${PROJECT_DIR}"
    git pull
else
    # If it doesn't exist, clone the repository
    git clone "https://github.com/${GITHUB_USERNAME}/${GITHUB_REPO}.git" "${PROJECT_DIR}"
fi

# Navigate to the project folder
cd "${PROJECT_DIR}"

# Install requirements from the requirements.txt file
sudo pip3 install -r requirements.txt

# Run the Flask app
# For development use:
python3 "${FLASK_APP}"

# For production use:
# sudo pip3 install gunicorn
# gunicorn -b 0.0.0.0:5000 "${FLASK_APP%%.*}:app" --daemon

# Note: Running the server with Gunicorn is recommended for production environments.