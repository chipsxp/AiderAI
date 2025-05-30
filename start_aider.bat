@echo off
echo Starting Aider...

:: Path to your virtual environment from system environment variable
if defined AIDER_PATH (
    set VENV_PATH=%AIDER_PATH%
) else (
    :: Fallback to a default path if AIDER_PATH is not set
    set VENV_PATH=%USERPROFILE%\GitHub\AiderAI
    echo AIDER_PATH environment variable not found. Using default: %VENV_PATH%
)

:: Create directory if it doesn't exist
if not exist %VENV_PATH% (
    echo Creating directory %VENV_PATH%...
    mkdir %VENV_PATH%
)

:: Check if virtual environment exists
if not exist %VENV_PATH%\Scripts\activate.bat (
    echo Creating virtual environment...
    python -m venv %VENV_PATH%
    call %VENV_PATH%\Scripts\activate.bat
    pip install pyyaml
    pip install aider-chat
    pip install pytest-playwright
    pip install watchdog
    pip install pathlib
) else (
    call %VENV_PATH%\Scripts\activate.bat
)

:: Start the agent communication system
echo Starting agent communication system...
start python agent_communication.py

:: Run the aider configuration script
python aider_config.py

:: Keep the window open until user presses a key
pause
