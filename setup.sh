#!/bin/bash

# This script sets up a Python virtual environment and installs the dependencies listed in requirements.txt
# It is optional, but recommended to avoid conflicts with your system Python packages

# Step 1: Create a virtual environment in the folder ".venv"
python3 -m venv .venv

# Step 2: Activate the virtual environment
# This ensures that Python and pip will use the isolated environment
source .venv/bin/activate

# Step 3: Install all the required Python packages from requirements.txt
pip install -r requirements.txt

# Done! The environment is ready.
echo "✅ Setup complete. Your virtual environment is ready. Use 'source .venv/bin/activate' to activate it later."
