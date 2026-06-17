from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from tejodaya.core.engine import TejodayaEngine
from tejodaya.agents.ai_creation import AICreationAgent
from tejodaya.agents.automation import AutomationAgent
from tejodaya.agents.research import ResearchAgent
from tejodaya.agents.system_control import SystemControlAgent
from tejodaya.agents.project_tracking import ProjectTrackingAgent
from tejodaya.agents.expanded_agents import MediaAgent, SocialMediaAgent, SecurityAgent
from tejodaya.agents.engineering import EngineeringAgent
from tejodaya.agents.learning import LearningAgent
from tejodaya.agents.hardware_agent import HardwareAgent
from tejodaya.agents.software_agent import SoftwareAgent
from tejodaya.agents.java_bridge import JavaAgentBridge
from tejodaya.agents.life_management import LifeManagementAgent
from tejodaya.agents.health import HealthAgent
from tejodaya.agents.discipline import DisciplineAgent
from tejodaya.agents.coach import CoachAgent
from tejodaya.core.memory import TejodayaMemory
import os

app = Flask(__name__)
CORS(app)

# Security: In a real app, use environment variables.
API_TOKEN = "tejodaya_secure_token_2026"

# Initialize Engine, Memory and Agents
memory = TejodayaMemory()
engine = TejodayaEngine()
engine.set_memory(memory)

engine.register_agent("AICreationAgent", AICreationAgent(engine))
engine.register_agent("AutomationAgent", AutomationAgent(engine))
engine.register_agent("ResearchAgent", ResearchAgent(engine))
engine.register_agent("SystemControlAgent", SystemControlAgent(engine))
engine.register_agent("ProjectTrackingAgent", ProjectTrackingAgent(engine))
engine.register_agent("MediaAgent", MediaAgent(engine))
engine.register_agent("SocialMediaAgent", SocialMediaAgent(engine))
engine.register_agent("SecurityAgent", SecurityAgent(engine))
engine.register_agent("EngineeringAgent", EngineeringAgent(engine))
engine.register_agent("LearningAgent", LearningAgent(engine))
engine.register_agent("HardwareAgent", HardwareAgent(engine))
engine.register_agent("SoftwareAgent", SoftwareAgent(engine))
engine.register_agent("LifeManagementAgent", LifeManagementAgent(engine))
engine.register_agent("HealthAgent", HealthAgent(engine))
engine.register_agent("DisciplineAgent", DisciplineAgent(engine))
engine.register_agent("CoachAgent", CoachAgent(engine))
engine.register_agent("FreelancingAgent", JavaAgentBridge("FreelancingAgent", engine, "tejodaya.agents.FreelancingAgent"))
engine.register_agent("TradingAgent", JavaAgentBridge("TradingAgent", engine, "tejodaya.agents.TradingAgent"))

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

@app.route('/command', methods=['POST'])
def command():
    # Check for authentication
    auth_header = request.headers.get('Authorization')
    if auth_header != f"Bearer {API_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    user_input = data.get('command')
    if not user_input:
        return jsonify({"error": "No command provided"}), 400

    response = engine.route_task(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=5000)
