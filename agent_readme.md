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

### Directory Structure and Purpose

Each directory serves a specific purpose in the collaboration workflow:

1. **Agent-specific directories** (`agent_gpt4o/` and `agent_sonnet/`):
   - Private workspaces for each AI model
   - Files created or modified here are automatically shared
   - Each agent only sees files in its own directory and the shared workspace
   - Useful for model-specific tasks before sharing with other agents

2. **Shared workspace** (`shared_workspace/`):
   - Central repository for all shared files
   - Contains a `metadata.json` file tracking ownership and history
   - Acts as the "handoff point" between agents
   - All agents can access files here

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

When working with an agent in the Aider chat interface, you can use these commands:

### 1. Sharing Files

To explicitly share a file with the other agent:
```
!share filename.txt
```

This command:
- Copies the file from your agent's directory to the shared workspace
- Updates the metadata to mark you as the owner
- Makes the file available to other agents

Example usage:
```
User: Can you share the database schema with the other agent?
Agent: I'll share it right away.
!share database_schema.sql
File database_schema.sql shared successfully.
```

### 2. Requesting Files

To request a file from the shared workspace:
```
!request filename.txt
```

This command:
- Copies the file from the shared workspace to your agent's directory
- Updates the metadata to record that you've accessed the file
- Makes the file available in your agent's context

Example usage:
```
User: I need you to review the API documentation the other agent created.
Agent: Let me get that file.
!request api_documentation.md
File api_documentation.md retrieved successfully.
```

### 3. Listing Shared Files

To see all files available in the shared workspace:
```
!list-shared
```

This command:
- Shows all files in the shared workspace
- Displays ownership information
- Shows when files were last modified

Example usage:
```
User: What files are available in the shared workspace?
Agent: Let me check.
!list-shared
Shared files:
- database_schema.sql (Owner: gpt-4o, Last modified: 2023-06-15 14:30)
- api_documentation.md (Owner: sonnet, Last modified: 2023-06-15 15:45)
```

## Collaborative Workflows

This system enables several powerful workflows when working with multiple AI models:

### Specialized Tasks

Assign different parts of a project to the model best suited for the task:
- Use GPT-4o for creative coding and complex problem-solving
- Use Claude Sonnet for documentation, explanations, and code reviews
- Share results between models to combine their strengths

### Code Review Workflow

1. Have one agent write code in its directory
2. The code is automatically shared to the shared workspace
3. Request the other agent to review the code
4. The reviewing agent can suggest improvements and share back the updated version

### Documentation Generation

1. Develop code with one agent
2. Share the completed code with the documentation specialist agent
3. The second agent creates comprehensive documentation
4. Both code and documentation are available in the shared workspace

### Iterative Development

1. Start a project with one agent
2. Share progress with the second agent for a fresh perspective
3. Continue development with either agent based on project needs
4. Maintain a complete history of changes in the shared workspace

## Troubleshooting

If you encounter issues with file sharing:

1. Check that both agents are running
2. Verify that the directories exist
3. Check the metadata.json file for file status
4. Restart the agents if necessary

## Advanced Usage

### Working with Multiple Files

You can share and request multiple files by using multiple commands:
```
!share file1.py
!share file2.py
!share file3.py
```

### Project Organization

For larger projects, consider creating subdirectories within each agent's directory:
- `agent_gpt4o/frontend/` for frontend code
- `agent_sonnet/documentation/` for documentation files

The file watcher will still detect changes and share files appropriately.
