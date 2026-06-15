import sys
from jarvis.core.engine import JarvisEngine
from jarvis.agents.ai_creation import AICreationAgent
from jarvis.agents.automation import AutomationAgent
from jarvis.agents.research import ResearchAgent
from jarvis.agents.java_bridge import JavaAgentBridge

def main():
    engine = JarvisEngine()

    # Register agents
    engine.register_agent("AICreationAgent", AICreationAgent(engine))
    engine.register_agent("AutomationAgent", AutomationAgent(engine))
    engine.register_agent("ResearchAgent", ResearchAgent(engine))
    engine.register_agent("FreelancingAgent", JavaAgentBridge("FreelancingAgent", engine, "jarvis.agents.FreelancingAgent"))
    engine.register_agent("TradingAgent", JavaAgentBridge("TradingAgent", engine, "jarvis.agents.TradingAgent"))

    print("JARVIS Terminal Interface")
    print("Type 'exit' to quit.")

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() == 'exit':
                break

            response = engine.route_task(user_input)
            print(f"JARVIS: {response}")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
