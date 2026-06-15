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
        import psutil
        try:
            # Using cross-platform psutil instead of shell commands
            processes = [f"{p.info['pid']}: {p.info['name']}" for p in psutil.process_iter(['pid', 'name'])]
            return "\n".join(processes[:20]) + "..."
        except Exception as e:
            return str(e)

    def run_shell_command(self, command):
        import platform
        # Security: Raw shell is requested, but we restrict it to a set of 'safe' commands for demo.
        # In a real absolute loyalty JARVIS, we would trust the owner.
        safe_commands = ["ls", "ps", "df", "ifconfig", "whoami", "date", "uptime", "tasklist", "dir", "ipconfig"]
        cmd_base = command.split()[0] if command.split() else ""

        if cmd_base not in safe_commands:
            return f"Security Restriction: Command '{cmd_base}' is not in the allowed list for remote execution."

        try:
            # Use list-based subprocess for safety against basic injection
            result = subprocess.check_output(command.split(), stderr=subprocess.STDOUT, text=True)
            return result
        except subprocess.CalledProcessError as e:
            return f"Command failed: {e.output}"
        except Exception as e:
            return f"Execution Error: {str(e)}"
