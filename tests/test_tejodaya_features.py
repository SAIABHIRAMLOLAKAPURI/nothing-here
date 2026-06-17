import pytest
from tejodaya.core.engine import TejodayaEngine
from tejodaya.core.memory import TejodayaMemory
from tejodaya.agents.life_management import LifeManagementAgent
from tejodaya.agents.health import HealthAgent
from tejodaya.agents.discipline import DisciplineAgent
from tejodaya.agents.coach import CoachAgent

@pytest.fixture
def engine():
    e = TejodayaEngine()
    m = TejodayaMemory(storage_path="tests/data/memory_test/")
    e.set_memory(m)
    return e

def test_life_management_agent(engine):
    agent = LifeManagementAgent(engine)
    engine.register_agent("LifeManagementAgent", agent)

    resp = agent.execute("add task Study Rust")
    assert "Study Rust" in resp
    assert len(engine.memory.get_tasks()) == 1

    resp = agent.execute("list tasks")
    assert "Study Rust" in resp

    resp = agent.execute("generate timetable")
    assert "Study Rust" in resp

def test_health_agent(engine):
    agent = HealthAgent(engine)
    resp = agent.execute("log meal Pizza")
    assert "Pizza" in resp
    assert len(engine.memory.long_term["nutrition"]["logs"]) == 1

    resp = agent.execute("nutrition report")
    assert "1 entries" in resp

def test_discipline_agent(engine):
    agent = DisciplineAgent(engine)
    agent.execute("add habit Reading")
    resp = agent.execute("track habit Reading")
    assert "streak for 'Reading' is now 1" in resp

    resp = agent.execute("discipline score")
    assert "Discipline Score" in resp

def test_coach_agent(engine):
    agent = CoachAgent(engine)
    resp = agent.execute("give me feedback")
    # The agent might not use the word "feedback" in the response if it goes to the suggestion branch
    assert "Sir" in resp
    assert "completion rate" in resp.lower() or "recommend" in resp.lower() or "review" in resp.lower()
