import sys
from tejodaya.core.engine import TejodayaEngine
from tejodaya.agents.ai_creation import AICreationAgent
from tejodaya.agents.automation import AutomationAgent
from tejodaya.agents.research import ResearchAgent
from tejodaya.agents.java_bridge import JavaAgentBridge

def main():
    engine = TejodayaEngine()

    # Register agents
    engine.register_agent("AICreationAgent", AICreationAgent(engine))
    engine.register_agent("AutomationAgent", AutomationAgent(engine))
    engine.register_agent("ResearchAgent", ResearchAgent(engine))
    engine.register_agent("FreelancingAgent", JavaAgentBridge("FreelancingAgent", engine, "tejodaya.agents.FreelancingAgent"))
    engine.register_agent("TradingAgent", JavaAgentBridge("TradingAgent", engine, "tejodaya.agents.TradingAgent"))

    print("Tejodaya Terminal Interface")
    print("Type 'exit' to quit.")

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() == 'exit':
                break

            response = engine.route_task(user_input)
            print(f"Tejodaya: {response}")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
