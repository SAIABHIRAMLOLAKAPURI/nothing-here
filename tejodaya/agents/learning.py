from tejodaya.agents.base import BaseAgent

class LearningAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("LearningAgent", engine)

    def execute(self, task):
        self.log(f"Processing Learning task: {task}")
        input_lower = task.lower()

        # Conversational / Greetings
        greetings = ["hello", "hi ", "hey", "good morning", "good evening", "how are you"]
        if any(g in input_lower for g in greetings):
            return "Hello Sir. I am Tejodaya, your personal AI assistant. How may I assist you today?"

        if "who are you" in input_lower:
            return "I am Tejodaya, a Just A Rather Very Intelligent System. I am your personal assistant, with absolute loyalty to you."

        if "what can you do" in input_lower:
            return "I can manage your system, perform research, analyze markets, assist with engineering, track projects, and learn new information as needed."

        # Learning logic
        if "learn that" in input_lower:
            parts = task.split("learn that")[-1].strip().split("is")
            if len(parts) >= 2:
                topic = parts[0].strip()
                fact = " ".join(parts[1:]).strip()
                self.engine.memory.store_knowledge(topic, fact)
                return f"Understood, Sir. I have recorded that {topic} is {fact}."
            return "I'm sorry Sir, I didn't catch the fact clearly. Please use the format: learn that [topic] is [fact]."

        elif "explain" in input_lower or "what is" in input_lower or "what are" in input_lower:
            topic = task.replace("explain", "").replace("what is", "").replace("what are", "").strip(" ?").lower()
            knowledge = self.engine.memory.get_knowledge(topic)
            if knowledge:
                return f"Based on my knowledge, {topic} is: {knowledge}"
            return f"Sir, I do not have specific records for '{topic}' in my database. Should I perform a web research for you?"

        return f"Learning Agent: I am listening and evolving, Sir. Task received: {task}"
