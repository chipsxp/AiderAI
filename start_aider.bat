@echo off
echo Starting Aider...

:: Path to your virtual environment - update this to your actual path
set VENV_PATH=C:\Users\CHIPSXPNFT\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312

:: Check if virtual environment exists
if not exist %VENV_PATH% (
    echo Creating virtual environment...
    python -m venv %VENV_PATH%
    call %VENV_PATH%\Scripts\activate
    pip install pyyaml
    pip install aider-chat
) else (
    call %VENV_PATH%\Scripts\activate
)

:: Run the aider configuration script
python aider_config.py

:: Keep the window open until user presses a key
pause