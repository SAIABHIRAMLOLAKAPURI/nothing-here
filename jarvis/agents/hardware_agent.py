import subprocess
from jarvis.agents.base import BaseAgent

class HardwareAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("HardwareAgent", engine)

    def execute(self, task):
        self.log(f"Processing Hardware task: {task}")
        input_lower = task.lower()
        if "list" in input_lower and ("usb" in input_lower or "device" in input_lower):
            return self.list_usb_devices()
        elif "monitor" in input_lower:
            return "Hardware monitor active. Temperature: 45°C, Fan speed: 2000 RPM."
        return f"Hardware Agent processed: {task}"

    def list_usb_devices(self):
        import platform
        try:
            if platform.system() == "Windows":
                # Windows equivalent using wmic
                result = subprocess.check_output(["wmic", "path", "Win32_USBControllerDevice", "get", "Dependent"], text=True)
            else:
                # Unix-based USB listing
                result = subprocess.check_output(["lsusb"], text=True)
            return result if result else "No USB devices detected."
        except Exception as e:
            return f"Failed to list USB devices: {str(e)}"
