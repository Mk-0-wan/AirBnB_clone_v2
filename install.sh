#!/usr/bin/env bash
# Install Fabric3 and its dependencies

# install python3.8
sudo apt update
sudo apt install software-properties-common

#Add the deadsnakes PPA to your sysmtem's source list
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install python3.8  python3.8-venv -y

python3.8 -m venv venv

# source the vertual enviroment
source venv/bin/activate

# uninstall fabric if it's already exist
pip3 uninstall -y Fabric

# install dependencies
sudo apt-get update
sudo apt-get install -y libffi-dev libssl-dev build-essential python3.8-dev libpython3-dev

packages=(
    "pyparsing"
    "appdirs"
    "setuptools==40.1.0"
    "cryptography==2.8"
    "bcrypt==3.1.7"
    "PyNaCl==1.3.0"
    "Fabric3==1.14.post1"
)

# Install Python packages
for package in "${packages[@]}"; do
    pip install --force-reinstall "$package"
done

echo "Installation completed successfully."
