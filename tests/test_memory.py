import pytest
from memory import add_to_memory, load_memory, save_memory

def test_add_to_memory_increases_length(tmp_path):
    mem_file = tmp_path / "memory.json"
    save_memory([], str(mem_file))
    add_to_memory("user", "hello", str(mem_file))
    data = load_memory(str(mem_file))
    assert len(data) == 1

def test_memory_saves_correct_role(tmp_path):
    mem_file = tmp_path / "memory.json"
    save_memory([], str(mem_file))
    add_to_memory("assistant", "hi mumma", str(mem_file))
    data = load_memory(str(mem_file))
    assert data[0]["role"] == "assistant"

def test_load_empty_memory(tmp_path):
    mem_file = tmp_path / "memory.json"
    save_memory([], str(mem_file))
    assert load_memory(str(mem_file)) == []