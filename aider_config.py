# Configuration file for storing API keys and managing agent communication

import yaml
import subprocess
import os
import argparse
from concurrent.futures import ThreadPoolExecutor
from agent_communication import SharedWorkspace, start_file_watcher, stop_file_watcher

def load_api_key(model_name):
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    if model_name == "gpt-4o":
        return config.get('openai-api-key')
    elif model_name == "sonnet":
        return config.get('anthropic-api-key')
    return None

def setup_agent_directories():
    """Set up the directory structure for agent communication"""
    shared_workspace = SharedWorkspace()
    print(f"Agent directories set up:")
    print(f"  GPT-4o: {shared_workspace.gpt4o_dir}")
    print(f"  Sonnet: {shared_workspace.sonnet_dir}")
    print(f"  Shared: {shared_workspace.shared_dir}")
    return shared_workspace

def run_aider_with_model(model, api_key, shared_workspace):
    """Run aider with the specified model and API key"""
    # Set up the working directory based on the model
    if model == "gpt-4o":
        working_dir = shared_workspace.gpt4o_dir
    elif model == "sonnet":
        working_dir = shared_workspace.sonnet_dir
    else:
        working_dir = "."
        
    # Create the directory if it doesn't exist
    os.makedirs(working_dir, exist_ok=True)
    
    # Start file watcher for this agent
    observer = start_file_watcher(model)
    
    try:
        # Change to the agent's working directory
        os.chdir(working_dir)
        
        # Run aider with the appropriate configuration
        if model == "gpt-4o":
            subprocess.run([
                "aider", 
                "--openai-api-key", api_key, 
                "--architect", 
                "--model", model, 
                "--watch-files", 
                "--browser"
            ])
        elif model == "sonnet":
            subprocess.run([
                "aider", 
                "--anthropic-api-key", api_key, 
                "--editor-model", model, 
                "--watch-files", 
                "--browser"
            ])
    finally:
        # Return to the original directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # Stop the file watcher
        stop_file_watcher(observer)

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Run Aider with different models')
    parser.add_argument('--model', choices=['gpt-4o', 'sonnet', 'both'], default='both',
                        help='Specify which model to run (default: both)')
    return parser.parse_args()

# Main execution
if __name__ == "__main__":
    args = parse_arguments()
    
    # Set up the shared workspace for agent communication
    shared_workspace = setup_agent_directories()
    
    # Determine which models to run
    if args.model == 'both':
        models = ["gpt-4o", "sonnet"]
    else:
        models = [args.model]
    
    print(f"Starting Aider with models: {', '.join(models)}")
    
    # Run Aider with the API key for each model concurrently through Pool Executor
    with ThreadPoolExecutor() as executor:
        futures = []
        for model in models:
            api_key = load_api_key(model)
            print(f"Loaded API Key for {model}: {api_key}")

            if api_key:
                futures.append(executor.submit(
                    run_aider_with_model, 
                    model, 
                    api_key, 
                    shared_workspace
                ))

        for future in futures:
            future.result()
