# Aider Multi-Model Launcher

This repository provides a flexible and easy-to-use setup for running the [Aider](https://github.com/paul-gauthier/aider) AI coding assistant. It allows you to easily switch between different large language models (like GPT-4o and Claude Sonnet) and manage your API keys securely.

## Features

- **Multi-Model Support**: Easily launch Aider with different AI models.
- **Centralized Configuration**: A single `config.yaml` file manages all your API keys and settings.
- **One-Click Start**: A simple batch script for Windows (`start_aider.bat`) automates the entire setup and launch process.
- **Automatic Environment Setup**: The script handles the creation of a Python virtual environment and installation of dependencies.
- **Browser-Based UI**: Launches Aider with the web browser interface enabled by default for a richer user experience.

## Prerequisites

- Python 3.8 or higher.
- Valid API keys for the AI models you intend to use (e.g., OpenAI, Anthropic).

## Setup and Usage

1.  **Clone the Repository**:
    ```sh
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Configure API Keys**:
    Create a `config.yaml` file in the root of the project. You can copy the example below and replace the placeholder values with your actual API keys.

3.  **Launch Aider**:
    Simply double-click the `start_aider.bat` file. It will:
    - Create a local Python virtual environment (`.venv`).
    - Install the necessary dependencies (`PyYAML` and `aider-chat`).
    - Run the `aider_config.py` script to start Aider with your configuration.

## Project Components

### config.yaml

This file is the central hub for your API keys and Aider settings. It must be present for the launcher script to work.

**Example `config.yaml`:**

```yaml
# API Keys (replace with your actual keys)
openai-api-key: your_openai_api_key_here
anthropic-api-key: your_anthropic_api_key_here
 
# Settings
gatherUsageStats: true
```

### aider_config.py

This Python script reads the configuration from `config.yaml` and launches Aider with the appropriate settings:

- Supports multiple AI models (GPT-4o and Claude Sonnet)
- Launches with browser interface enabled
- Uses ThreadPoolExecutor for concurrent model launching

The script automatically selects the correct API key based on the model being used.

### start_aider.bat

A Windows batch script that:

1. Creates and activates a Python virtual environment if one doesn't exist
2. Installs required dependencies (PyYAML and aider-chat)
3. Runs the `aider_config.py` script

Simply double-click this file to launch Aider with your configured settings.

## Setup Instructions

1. Clone this repository
2. Create a `config.yaml` file with your API keys (see example above)
3. Double-click `start_aider.bat` to launch Aider

## Requirements

- Python 3.8 or higher
- Internet connection for API access
- Valid API keys for your preferred AI models

## Notes

- The `config.yaml` file is added to `.gitignore` to prevent accidentally committing your API keys
- For security, never share your API keys or commit them to public repositories