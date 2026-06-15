import pytest
from jarvis.core.engine import JarvisEngine
from jarvis.agents.ai_creation import AICreationAgent
from jarvis.agents.automation import AutomationAgent
from jarvis.agents.research import ResearchAgent
from jarvis.agents.java_bridge import JavaAgentBridge
import subprocess

@pytest.fixture
def engine():
    return JarvisEngine()

def test_python_agents(engine):
    ai_agent = AICreationAgent(engine)
    engine.register_agent("AICreationAgent", ai_agent)

    response = engine.route_task("Write code for a neural network")
    assert "Generated code" in response

def test_java_bridge(engine):
    # Ensure Java is compiled
    subprocess.run(["javac", "-d", "jarvis/agents/java", "jarvis/agents/java/FreelancingAgent.java"])

    freelance_agent = JavaAgentBridge("FreelancingAgent", engine, "jarvis.agents.FreelancingAgent")
    engine.register_agent("FreelancingAgent", freelance_agent)

    response = engine.route_task("Find a job")
    assert "Freelancing Agent" in response
    assert "jobs" in response
