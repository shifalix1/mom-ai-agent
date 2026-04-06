import json
import os

MEMORY_FILE = "memory.json"

def load_memory(file_path=MEMORY_FILE):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def save_memory(messages, file_path=MEMORY_FILE):
    with open(file_path, "w") as f:
        json.dump(messages, f, indent=2)

def add_to_memory(role, content, file_path=MEMORY_FILE):
    messages = load_memory(file_path)
    messages.append({"role": role, "content": content})
    save_memory(messages, file_path)