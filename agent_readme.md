# Aider Agent Communication System

This system allows two different AI agents (GPT-4o and Sonnet) to share files and collaborate on projects.

## Setup

1. Make sure you have a `config.yaml` file with your API keys:
   ```yaml
   openai-api-key: "your-openai-api-key"
   anthropic-api-key: "your-anthropic-api-key"
   ```

2. Run the start_aider.bat script to launch both agents:
   ```
   start_aider.bat
   ```

3. To run only one specific agent:
   ```
   start_aider.bat gpt-4o
   ```
   or
   ```
   start_aider.bat sonnet
   ```

## How File Sharing Works

The system creates three directories:
- `agent_gpt4o/`: Working directory for the GPT-4o agent
- `agent_sonnet/`: Working directory for the Sonnet agent
- `shared_workspace/`: Directory where files are shared between agents

### Sharing Files

Files are automatically shared when they are modified in an agent's directory. You can also manually share files by:

1. Creating or modifying a file in an agent's directory
2. The file will automatically be copied to the shared workspace
3. The other agent can access the file from the shared workspace

### Metadata

The system maintains a metadata.json file in the shared workspace that tracks:
- Which agent owns each file
- When files were last modified
- Which agents have accessed each file

## Commands for Agents

When working with an agent, you can use these commands:

1. To share a file with the other agent:
   ```
   !share filename.txt
   ```

2. To request a file from the shared workspace:
   ```
   !request filename.txt
   ```

3. To list all shared files:
   ```
   !list-shared
   ```

## Troubleshooting

If you encounter issues with file sharing:

1. Check that both agents are running
2. Verify that the directories exist
3. Check the metadata.json file for file status
4. Restart the agents if necessary
