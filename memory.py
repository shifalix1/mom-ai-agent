import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(messages):
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)

def add_to_memory(role, content):
    messages = load_memory()
    messages.append({"role": role, "content": content})
    save_memory(messages)
    