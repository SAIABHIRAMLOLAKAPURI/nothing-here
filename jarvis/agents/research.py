from jarvis.agents.base import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("ResearchAgent", engine)

    def execute(self, task):
        self.log(f"Processing Research task: {task}")
        if "web" in task or "research" in task:
            return "Searching the web for information..."
        elif "summarize" in task:
            return "Summarizing document..."
        return f"Research Agent processed: {task}"
