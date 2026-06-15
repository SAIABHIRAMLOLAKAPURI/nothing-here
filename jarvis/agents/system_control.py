import subprocess
from jarvis.agents.base import BaseAgent

class SystemControlAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("SystemControlAgent", engine)

    def execute(self, task):
        self.log(f"Executing system command: {task}")
        if "process" in task:
            return self.monitor_processes()
        elif "shell" in task:
            command = task.split("shell")[-1].strip()
            return self.run_shell_command(command)
        return f"System Control Agent processed: {task}"

    def monitor_processes(self):
        try:
            result = subprocess.check_output(["ps", "aux"], text=True)
            return result[:500] + "..." # Truncated for brevity
        except Exception as e:
            return str(e)

    def run_shell_command(self, command):
        # EXTREME CAUTION: This gives absolute control as requested.
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            return result
        except subprocess.CalledProcessError as e:
            return f"Command failed: {e.output}"
