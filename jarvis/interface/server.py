from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from jarvis.core.engine import JarvisEngine
from jarvis.agents.ai_creation import AICreationAgent
from jarvis.agents.automation import AutomationAgent
from jarvis.agents.research import ResearchAgent
from jarvis.agents.system_control import SystemControlAgent
from jarvis.agents.java_bridge import JavaAgentBridge
import os

app = Flask(__name__)
CORS(app)

# Initialize Engine and Agents
engine = JarvisEngine()
engine.register_agent("AICreationAgent", AICreationAgent(engine))
engine.register_agent("AutomationAgent", AutomationAgent(engine))
engine.register_agent("ResearchAgent", ResearchAgent(engine))
engine.register_agent("SystemControlAgent", SystemControlAgent(engine))
engine.register_agent("FreelancingAgent", JavaAgentBridge("FreelancingAgent", engine, "jarvis.agents.FreelancingAgent"))
engine.register_agent("TradingAgent", JavaAgentBridge("TradingAgent", engine, "jarvis.agents.TradingAgent"))

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    user_input = data.get('command')
    if not user_input:
        return jsonify({"error": "No command provided"}), 400

    response = engine.route_task(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    # Serve from jarvis/interface directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app.run(port=5000)
