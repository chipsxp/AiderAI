@echo off
echo Starting Aider with Agent Communication...

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
) else (
    call %VENV_PATH%\Scripts\activate.bat
)

:: Parse command line arguments
set MODEL=both
if not "%1"=="" (
    if "%1"=="gpt-4o" (
        set MODEL=gpt-4o
    ) else if "%1"=="sonnet" (
        set MODEL=sonnet
    )
)

:: Run the aider configuration script with the specified model
python aider_config.py --model %MODEL%

:: Keep the window open until user presses a key
pause
