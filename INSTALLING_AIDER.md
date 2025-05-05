# Installing Aider

This guide provides instructions for installing Aider, an AI pair programming tool. The information is sourced from the [official Aider installation documentation](https://aider.chat/docs/install.html).

## Prerequisites

Before installing Aider, ensure you have:

- Python 3.8 or newer
- Git (required for most functionality)
- An OpenAI API key or Anthropic API key

## Installation Methods

### Standard Installation

The simplest way to install Aider is using pip:

```bash
python -m pip install aider-install
aider-install
```
Install with uv
You can install aider with uv:

```bash
python -m pip install uv  # If you need to install uv
uv tool install --force --python python3.12 aider-chat@latest
```

### Installation with pip (older versions)

```bash
pip install aider-chat
```

### Installation with Browser Interface

To install Aider with the browser interface:

```bash
pip install "aider-chat[browser]"
```

### Installation with Voice Support

To install Aider with voice support:

```bash
pip install "aider-chat[voice]"
```

### Installation with All Features

To install Aider with all optional features:

```bash
pip install "aider-chat[all]"
```

## Verifying Installation

After installation, you can verify that Aider is working by running:

```bash
aider --help
```

## API Keys

Aider requires an API key to function. You can provide your API key in several ways:

1. As a command-line argument: `aider --openai-api-key sk-...`
2. As an environment variable: `export OPENAI_API_KEY=sk-...`
3. In a configuration file (as described in our main README)

## Updating Aider

To update Aider to the latest version:

```bash
pip install --upgrade aider-chat
```

## Troubleshooting

If you encounter issues during installation:

1. Ensure you have the latest version of pip: `pip install --upgrade pip`
2. Check that you meet all prerequisites
3. For platform-specific issues, refer to the [official documentation](https://aider.chat/docs/install.html)

## Additional Resources

- [Aider Documentation](https://aider.chat/docs/)
- [GitHub Repository](https://github.com/paul-gauthier/aider)