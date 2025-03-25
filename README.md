# Aider Configuration Setup

This repository contains configuration and scripts to easily launch Aider, an AI-powered coding assistant, with your preferred models and settings.

## Required Files

### config.yaml

This YAML configuration file stores your API keys and settings. **This file is required for the scripts to work properly.**

Example `config.yaml`:

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