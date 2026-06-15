import os
from jarvis.agents.base import BaseAgent

class AutomationAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("AutomationAgent", engine)

    def execute(self, task):
        self.log(f"Processing Automation task: {task}")
        input_lower = task.lower()
        if "list files" in input_lower:
            return str(os.listdir("."))
        elif "current directory" in input_lower:
            return os.getcwd()
        elif "disk usage" in input_lower:
            import shutil
            total, used, free = shutil.disk_usage("/")
            return f"Total: {total // (2**30)}GB, Used: {used // (2**30)}GB, Free: {free // (2**30)}GB"
        elif "file" in task or "folder" in task:
            return "Managing files and folders... (Generic)"
        return f"Automation Agent processed: {task}"
