from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from jarvis.core.engine import JarvisEngine
from jarvis.agents.ai_creation import AICreationAgent
from jarvis.agents.automation import AutomationAgent
from jarvis.agents.research import ResearchAgent
from jarvis.agents.system_control import SystemControlAgent
from jarvis.agents.project_tracking import ProjectTrackingAgent
from jarvis.agents.expanded_agents import MediaAgent, SocialMediaAgent, SecurityAgent
from jarvis.agents.engineering import EngineeringAgent
from jarvis.agents.learning import LearningAgent
from jarvis.agents.hardware_agent import HardwareAgent
from jarvis.agents.software_agent import SoftwareAgent
from jarvis.agents.java_bridge import JavaAgentBridge
import os

app = Flask(__name__)
CORS(app)

# Security: In a real app, use environment variables.
API_TOKEN = "jarvis_secure_token_2026"

# Initialize Engine and Agents
engine = JarvisEngine()
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
engine.register_agent("FreelancingAgent", JavaAgentBridge("FreelancingAgent", engine, "jarvis.agents.FreelancingAgent"))
engine.register_agent("TradingAgent", JavaAgentBridge("TradingAgent", engine, "jarvis.agents.TradingAgent"))

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
