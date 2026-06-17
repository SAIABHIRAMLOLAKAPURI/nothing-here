import pytest
from tejodaya.core.engine import TejodayaEngine
from tejodaya.agents.ai_creation import AICreationAgent
from tejodaya.agents.automation import AutomationAgent
from tejodaya.agents.research import ResearchAgent
from tejodaya.agents.java_bridge import JavaAgentBridge
import subprocess

@pytest.fixture
def engine():
    return TejodayaEngine()

def test_python_agents(engine):
    ai_agent = AICreationAgent(engine)
    engine.register_agent("AICreationAgent", ai_agent)

    response = engine.route_task("Write code for a neural network")
    # Updated to match the refined Tejodaya personality
    assert "generated" in response.lower()

def test_java_bridge(engine):
    # Ensure Java is compiled
    subprocess.run(["javac", "-d", "tejodaya/agents/java", "tejodaya/agents/java/FreelancingAgent.java"])

    freelance_agent = JavaAgentBridge("FreelancingAgent", engine, "tejodaya.agents.FreelancingAgent")
    engine.register_agent("FreelancingAgent", freelance_agent)

    response = engine.route_task("Find a job")
    assert "Freelancing Agent" in response
    assert "jobs" in response
