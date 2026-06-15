from jarvis.core.engine import JarvisEngine
from jarvis.agents.ai_creation import AICreationAgent
from jarvis.agents.java_bridge import JavaAgentBridge

def test_agents():
    engine = JarvisEngine()

    # Register Python agent
    ai_agent = AICreationAgent(engine)
    engine.register_agent("AICreationAgent", ai_agent)

    # Register Java agent via bridge
    freelance_agent = JavaAgentBridge("FreelancingAgent", engine, "jarvis.agents.FreelancingAgent")
    engine.register_agent("FreelancingAgent", freelance_agent)

    # Test routing to Python
    resp1 = engine.route_task("Write some code")
    print(f"Python Agent Response: {resp1}")

    # Test routing to Java
    resp2 = engine.route_task("Find a freelance job")
    print(f"Java Agent Response: {resp2}")

if __name__ == "__main__":
    test_agents()
