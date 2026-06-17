import subprocess
import platform
import psutil
import time
from tejodaya.agents.base import BaseAgent

class SystemControlAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("SystemControlAgent", engine)

    def execute(self, task):
        self.log(f"Executing system command: {task}")
        input_lower = task.lower()
        if "process" in input_lower:
            return self.monitor_processes()
        elif "status report" in input_lower or "system status" in input_lower:
            return self.get_status_report()
        elif "shell" in input_lower:
            command = task.split("shell")[-1].strip()
            return self.run_shell_command(command)
        return f"System Control Agent processed: {task}"

    def get_status_report(self):
        boot_time = psutil.boot_time()
        uptime = time.time() - boot_time
        hours, rem = divmod(uptime, 3600)
        minutes, seconds = divmod(rem, 60)

        report = [
            f"System Status Report:",
            f"OS: {platform.system()} {platform.release()}",
            f"Uptime: {int(hours)}h {int(minutes)}m {int(seconds)}s",
            f"CPU Usage: {psutil.cpu_percent()}%",
            f"Memory Usage: {psutil.virtual_memory().percent}%",
            f"Disk Usage: {psutil.disk_usage('/').percent}%"
        ]
        return "\n".join(report)

    def monitor_processes(self):
        try:
            processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']),
                             key=lambda p: p.info['cpu_percent'], reverse=True)
            output = ["Top Processes (CPU %):"]
            for p in processes[:10]:
                output.append(f"PID {p.info['pid']}: {p.info['name']} ({p.info['cpu_percent']}%)")
            return "\n".join(output)
        except Exception as e:
            return f"Process monitoring failed: {str(e)}"

    def run_shell_command(self, command):
        # In a real absolute loyalty Tejodaya, we would trust the owner.
        safe_commands = ["ls", "ps", "df", "ifconfig", "whoami", "date", "uptime", "tasklist", "dir", "ipconfig", "netstat", "echo"]
        cmd_parts = command.split()
        cmd_base = cmd_parts[0] if cmd_parts else ""

        if cmd_base not in safe_commands:
            return f"Security Restriction: Command '{cmd_base}' is restricted. Only authorized system commands are permitted."

        try:
            # Use shell=True for some Windows commands like 'dir'
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=5)
            return result.stdout if result.stdout else result.stderr
        except Exception as e:
            return f"Execution Error: {str(e)}"
