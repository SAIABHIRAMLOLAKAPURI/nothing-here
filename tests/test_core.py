import pytest
from tejodaya.core.engine import TejodayaEngine
from tejodaya.core.memory import TejodayaMemory
import os
import shutil

@pytest.fixture
def memory():
    test_path = "tests/data/memory/"
    if os.path.exists(test_path):
        shutil.rmtree(test_path)
    mem = TejodayaMemory(storage_path=test_path)
    yield mem
    if os.path.exists(test_path):
        shutil.rmtree(test_path)

def test_engine_init():
    engine = TejodayaEngine()
    assert engine.agents == {}
    assert engine.memory is None

def test_memory_persistence(memory):
    memory.set_preference("theme", "dark")
    assert memory.get_preference("theme") == "dark"

    # Reload memory
    memory2 = TejodayaMemory(storage_path="tests/data/memory/")
    assert memory2.get_preference("theme") == "dark"

def test_memory_short_term(memory):
    for i in range(15):
        memory.add_to_short_term(f"Interaction {i}")
    assert len(memory.short_term) == 10
    assert memory.short_term[-1] == "Interaction 14"
