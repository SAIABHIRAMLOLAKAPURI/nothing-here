from jarvis.agents.base import BaseAgent

class LearningAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("LearningAgent", engine)

    def execute(self, task):
        self.log(f"Processing Learning task: {task}")
        input_lower = task.lower()
        if "learn" in input_lower:
            # Simulated learning from a source
            topic = task.split("learn")[-1].strip()
            self.engine.memory.store_knowledge(topic, f"Knowledge about {topic} acquired through learning.")
            return f"I have successfully learned about: {topic}."
        elif "explain" in input_lower:
            topic = task.split("explain")[-1].strip()
            knowledge = self.engine.memory.get_knowledge(topic)
            return knowledge if knowledge else f"I do not have knowledge about '{topic}' yet. Should I learn it?"
        return f"Learning Agent processed: {task}"
