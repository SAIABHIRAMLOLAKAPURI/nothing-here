import os
import subprocess

def get_disk_usage():
    return subprocess.check_output(["df", "-h"], text=True)

def get_network_config():
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
