@echo off
REM This script sets up a Python virtual environment and installs the dependencies listed in requirements.txt
REM It is optional, but recommended to avoid conflicts with your system Python packages

REM Step 1: Create a virtual environment in the folder ".venv"
python -m venv .venv

REM Step 2: Activate the virtual environment
CALL .venv\Scripts\activate

REM Step 3: Install all the required Python packages from requirements.txt
pip install -r requirements.txt

ECHO ✅ Setup complete. Your virtual environment is ready.
ECHO Use ".venv\Scripts\activate" to activate it in the future.
