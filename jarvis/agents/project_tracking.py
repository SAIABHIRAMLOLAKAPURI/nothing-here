from jarvis.agents.base import BaseAgent

class ProjectTrackingAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("ProjectTrackingAgent", engine)

    def execute(self, task):
        self.log(f"Processing Project Tracking task: {task}")
        input_lower = task.lower()
        if "create project" in input_lower:
            project_name = task.split("project")[-1].strip()
            self.engine.memory.store_project_data(project_name, {"status": "started", "tasks": []})
            return f"Project '{project_name}' created."
        elif "status" in input_lower:
            project_name = task.split("status")[-1].strip()
            data = self.engine.memory.get_project_data(project_name)
            return f"Project '{project_name}' status: {data.get('status') if data else 'Not found'}"
        return f"Project Tracking Agent processed: {task}"
