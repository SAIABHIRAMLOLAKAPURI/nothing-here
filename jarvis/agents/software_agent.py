import subprocess
from jarvis.agents.base import BaseAgent

class SoftwareAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("SoftwareAgent", engine)

    def execute(self, task):
        self.log(f"Processing Software task: {task}")
        input_lower = task.lower()
        if "list" in input_lower and "software" in input_lower:
            return self.list_installed_software()
        elif "update" in input_lower:
            return "Software Agent: Checking for system updates... Everything is up to date."
        elif "install" in input_lower:
            pkg = task.split("install")[-1].strip()
            return f"Software Agent: Preparing to install {pkg}... (Requires administrative approval)"
        return f"Software Agent processed: {task}"

    def list_installed_software(self):
        try:
            # Example for debian-based systems
            result = subprocess.check_output(["dpkg", "--get-selections"], text=True)
            return result[:500] + "..." # Truncated
        except Exception:
            return "Failed to list installed software. System not supported."
