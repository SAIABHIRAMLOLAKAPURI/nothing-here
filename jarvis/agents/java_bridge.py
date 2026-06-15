import subprocess
import os
from jarvis.agents.base import BaseAgent

class JavaAgentBridge(BaseAgent):
    def __init__(self, name, engine, java_class):
        super().__init__(name, engine)
        self.java_class = java_class

    def execute(self, task):
        self.log(f"Delegating task to Java: {task}")
        classpath = os.path.join("jarvis", "agents", "java")
        try:
            # For long-running background tasks, we should use Popen or a service.
            # For now, we continue using check_output for synchronous requests,
            # but we allow specific "start" commands to use Popen.
            if "start_background" in task:
                subprocess.Popen(
                    ["java", "-cp", classpath, self.java_class, task],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                return f"Agent {self.name} started in background."

            result = subprocess.check_output(
                ["java", "-cp", classpath, self.java_class, task],
                stderr=subprocess.STDOUT,
                text=True
            )
            return result.strip()
        except subprocess.CalledProcessError as e:
            return f"Error executing Java agent {self.name}: {e.output}"
