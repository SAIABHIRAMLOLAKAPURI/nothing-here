from jarvis.core.engine import JarvisEngine
from jarvis.core.memory import JarvisMemory

def test_integration():
    engine = JarvisEngine()
    memory = JarvisMemory(storage_path="jarvis/data/test_memory/")
    engine.set_memory(memory)

    # Test memory
    memory.set_preference("loyalty", "absolute")
    assert memory.get_preference("loyalty") == "absolute"

    print("Core integration test passed!")

if __name__ == "__main__":
    test_integration()
