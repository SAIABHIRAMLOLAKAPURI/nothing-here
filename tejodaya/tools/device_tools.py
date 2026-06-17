import os
import subprocess
import platform

def get_disk_usage():
    if platform.system() == "Windows":
        return subprocess.check_output(["wmic", "logicaldisk", "get", "size,freespace,caption"], text=True)
    return subprocess.check_output(["df", "-h"], text=True)

def get_network_config():
    if platform.system() == "Windows":
        return subprocess.check_output(["ipconfig"], text=True)
    return subprocess.check_output(["ifconfig"], text=True)

def kill_process(pid):
    try:
        os.kill(pid, 9)
        return f"Process {pid} terminated."
    except Exception as e:
        return str(e)

def list_usb():
    return subprocess.check_output(["lsusb"], text=True)

def list_software():
    return subprocess.check_output(["dpkg", "--get-selections"], text=True)
