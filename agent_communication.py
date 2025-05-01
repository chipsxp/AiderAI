# Agent communication module for sharing files between aider instances
import os
import json
import time
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SharedWorkspace:
    def __init__(self, base_dir="."):
        """Initialize the shared workspace for agent communication"""
        self.base_dir = base_dir
        self.gpt4o_dir = os.path.join(base_dir, "agent_gpt4o")
        self.sonnet_dir = os.path.join(base_dir, "agent_sonnet")
        self.shared_dir = os.path.join(base_dir, "shared_workspace")
        
        # Create directories if they don't exist
        for directory in [self.gpt4o_dir, self.sonnet_dir, self.shared_dir]:
            os.makedirs(directory, exist_ok=True)
            
        # Create metadata file to track file ownership and status
        self.metadata_file = os.path.join(self.shared_dir, "metadata.json")
        if not os.path.exists(self.metadata_file):
            with open(self.metadata_file, 'w') as f:
                json.dump({"files": {}}, f)

    def share_file(self, source_path, agent_name):
        """Share a file from an agent's directory to the shared workspace"""
        if not os.path.exists(source_path):
            print(f"Error: File {source_path} does not exist")
            return False
            
        filename = os.path.basename(source_path)
        dest_path = os.path.join(self.shared_dir, filename)
        
        # Copy the file to shared workspace
        shutil.copy2(source_path, dest_path)
        
        # Update metadata
        with open(self.metadata_file, 'r') as f:
            metadata = json.load(f)
        
        metadata["files"][filename] = {
            "owner": agent_name,
            "last_modified": time.time(),
            "shared_with": [],
            "status": "shared"
        }
        
        with open(self.metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
            
        print(f"File {filename} shared by {agent_name}")
        return True
        
    def request_file(self, filename, requesting_agent):
        """Request a file from the shared workspace"""
        shared_file_path = os.path.join(self.shared_dir, filename)
        
        if not os.path.exists(shared_file_path):
            print(f"Error: File {filename} not found in shared workspace")
            return False
            
        # Determine destination based on requesting agent
        if requesting_agent == "gpt-4o":
            dest_dir = self.gpt4o_dir
        elif requesting_agent == "sonnet":
            dest_dir = self.sonnet_dir
        else:
            print(f"Error: Unknown agent {requesting_agent}")
            return False
            
        dest_path = os.path.join(dest_dir, filename)
        
        # Copy the file to the agent's directory
        shutil.copy2(shared_file_path, dest_path)
        
        # Update metadata
        with open(self.metadata_file, 'r') as f:
            metadata = json.load(f)
            
        if filename in metadata["files"]:
            if requesting_agent not in metadata["files"][filename]["shared_with"]:
                metadata["files"][filename]["shared_with"].append(requesting_agent)
                
            with open(self.metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
                
        print(f"File {filename} requested by {requesting_agent}")
        return True

class FileWatcher(FileSystemEventHandler):
    def __init__(self, shared_workspace, agent_name):
        self.shared_workspace = shared_workspace
        self.agent_name = agent_name
        
    def on_modified(self, event):
        if event.is_directory:
            return
            
        # Check if file is in agent's directory and not already in shared workspace
        if self.agent_name == "gpt-4o" and event.src_path.startswith(self.shared_workspace.gpt4o_dir):
            self.shared_workspace.share_file(event.src_path, "gpt-4o")
        elif self.agent_name == "sonnet" and event.src_path.startswith(self.shared_workspace.sonnet_dir):
            self.shared_workspace.share_file(event.src_path, "sonnet")

def start_file_watcher(agent_name):
    """Start a file watcher for the specified agent"""
    shared_workspace = SharedWorkspace()
    event_handler = FileWatcher(shared_workspace, agent_name)
    
    # Determine which directory to watch based on agent name
    if agent_name == "gpt-4o":
        watch_dir = shared_workspace.gpt4o_dir
    elif agent_name == "sonnet":
        watch_dir = shared_workspace.sonnet_dir
    else:
        print(f"Error: Unknown agent {agent_name}")
        return None
        
    observer = Observer()
    observer.schedule(event_handler, watch_dir, recursive=True)
    observer.start()
    
    print(f"File watcher started for {agent_name} in {watch_dir}")
    return observer

def stop_file_watcher(observer):
    """Stop the file watcher"""
    if observer:
        observer.stop()
        observer.join()
