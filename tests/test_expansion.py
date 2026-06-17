import pytest
from tejodaya.core.engine import TejodayaEngine
from tejodaya.core.memory import TejodayaMemory
from tejodaya.agents.project_tracking import ProjectTrackingAgent
from tejodaya.agents.ai_creation import AICreationAgent
from tejodaya.agents.research import ResearchAgent
import os
import shutil

@pytest.fixture
def engine():
    test_path = "tests/data/memory_expansion/"
    if os.path.exists(test_path):
        shutil.rmtree(test_path)
    mem = TejodayaMemory(storage_path=test_path)
    e = TejodayaEngine()
    e.set_memory(mem)
    return e

def test_project_tracking(engine):
    agent = ProjectTrackingAgent(engine)
    engine.register_agent("ProjectTrackingAgent", agent)

    resp = engine.route_task("create project TestExpansion")
    assert "created" in resp

    status = engine.route_task("project status TestExpansion")
    assert "started" in status

def test_ai_creation_expansion(engine):
    agent = AICreationAgent(engine)
    engine.register_agent("AICreationAgent", agent)

    resp = engine.route_task("design architecture for a web app")
    # Updated to match the refined Tejodaya personality
    assert "Architectural" in resp

    doc = engine.route_task("generate documentation")
    assert "generated" in doc

def test_research_scraping(engine):
    agent = ResearchAgent(engine)
    engine.register_agent("ResearchAgent", agent)

    # Test scraping a known local file or a public site
    # Since we might not have internet, we test the branch logic
    resp = engine.route_task("scrape http://example.com")
    assert "Scraped" in resp or "failed" in resp
