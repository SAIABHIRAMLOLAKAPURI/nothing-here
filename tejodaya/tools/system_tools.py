import os
import psutil

def get_system_status():
    cpu_usage = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    return {
        "cpu_usage": f"{cpu_usage}%",
        "memory_usage": f"{memory_info.percent}%"
    }

def list_files(path="."):
    return os.listdir(path)

def execute_script(script_path):
    # Basic validation to prevent simple command injection
    if ";" in script_path or "|" in script_path or "&" in script_path:
        return "Invalid script path."
    return os.system(f"python3 {script_path}")
