import logging

class JarvisEngine:
    def __init__(self):
        self.agents = {}
        self.memory = None
        self.logger = logging.getLogger("JarvisEngine")
        logging.basicConfig(level=logging.INFO)

    def register_agent(self, name, agent):
        self.agents[name] = agent
        self.logger.info(f"Agent {name} registered.")

    def set_memory(self, memory_module):
        self.memory = memory_module
        self.logger.info("Memory module linked.")

    def route_task(self, user_input):
        self.logger.info(f"Routing task: {user_input}")
        # Simple keyword-based routing for now
        input_lower = user_input.lower()

        if any(kw in input_lower for kw in ["code", "debug", "create agent", "architecture", "design", "documentation", "doc"]):
            return self.agents.get("AICreationAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["job", "freelance", "proposal", "client", "match"]):
            return self.agents.get("FreelancingAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["market", "trade", "stock", "price", "analyze", "trend"]):
            return self.agents.get("TradingAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["file", "folder", "automate", "system", "disk"]):
            return self.agents.get("AutomationAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["research", "summarize", "info", "gather", "scrape", "web"]):
            return self.agents.get("ResearchAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["project", "task", "track"]):
            return self.agents.get("ProjectTrackingAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["learn", "explain", "study"]):
            return self.agents.get("LearningAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["media", "play", "browse"]):
            return self.agents.get("MediaAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["social", "twitter", "linkedin", "post"]):
            return self.agents.get("SocialMediaAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["security", "hack", "audit"]):
            return self.agents.get("SecurityAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["cad", "catia", "fem", "engineering", "calculation"]):
            return self.agents.get("EngineeringAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["hardware", "usb", "monitor"]):
            return self.agents.get("HardwareAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["software", "install", "update", "package"]):
            return self.agents.get("SoftwareAgent").execute(user_input)
        elif any(kw in input_lower for kw in ["system", "shell", "process", "device", "control"]):
            return self.agents.get("SystemControlAgent").execute(user_input)
        else:
            return "I am not sure which agent should handle this task. Can you please clarify?"

    def coordinate_agents(self, task, participating_agents):
        self.logger.info(f"Coordinating complex task: {task} with agents: {participating_agents}")
        # Logic for multi-agent coordination would go here
        results = {}
        for agent_name in participating_agents:
            if agent_name in self.agents:
                results[agent_name] = self.agents[agent_name].execute(task)
        return results
