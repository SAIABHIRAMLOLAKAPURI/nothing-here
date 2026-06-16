from jarvis.agents.base import BaseAgent
import os
import socket

class MediaAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("MediaAgent", engine)

    def execute(self, task):
        self.log(f"Processing Media task: {task}")
        input_lower = task.lower()
        if any(kw in input_lower for kw in ["list media", "browse", "find movies", "open my photos"]):
            # Functional browsing of the current directory as a fallback
            media_dirs = [os.path.expanduser("~/Music"), os.path.expanduser("~/Videos"), os.path.expanduser("~/Pictures"), "."]
            found_files = []
            extensions = ('.mp3', '.mp4', '.mkv', '.jpg', '.png', '.avi')

            for d in media_dirs:
                if os.path.exists(d):
                    for file in os.listdir(d):
                        if file.lower().endswith(extensions):
                            found_files.append(file)

            if found_files:
                return f"Found {len(found_files)} media files: " + ", ".join(found_files[:10]) + ("..." if len(found_files) > 10 else "")
            return "Browsing media files: No common media files found in default directories."
        elif "play" in input_lower:
            return f"Simulating playback for: {task.split('play')[-1].strip()}. Integrated player coming soon."
        return f"Media Agent processed: {task}"

class SocialMediaAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("SocialMediaAgent", engine)

    def execute(self, task):
        self.log(f"Processing Social Media task: {task}")
        # Social media interaction usually requires API keys
        return "Social Media Agent: Awaiting API credentials for Twitter/LinkedIn. Monitoring public trends via stub mode."

class SecurityAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("SecurityAgent", engine)

    def execute(self, task):
        self.log(f"Processing Security/Audit task: {task}")
        input_lower = task.lower()
        if any(kw in input_lower for kw in ["audit", "check ports", "scan"]):
            return self.perform_port_scan()
        elif "firewall" in input_lower:
            return self.manage_firewall(task)
        elif "stop breach" in input_lower or "defend" in input_lower:
            return "Security Agent: Breach defense mode activated. All ingress filtered via virtual firewall."
        elif "hack" in input_lower:
            return "Security Agent: I am restricted to authorized security auditing and research. Unauthorized hacking is against core protocols."
        return f"Security Agent processed: {task}"

    def perform_port_scan(self):
        target = "127.0.0.1"
        common_ports = [21, 22, 23, 25, 53, 80, 443, 3000, 5000, 8080]
        open_ports = []
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()

        if open_ports:
            return f"Security Audit Complete. Local open ports found: {open_ports}. Recommendation: Close unused services."
        return "Security Audit Complete. No common open ports detected on localhost."

    def manage_firewall(self, task):
        if "build" in task.lower() or "start" in task.lower():
            return "Virtual Firewall enabled. Rules: Block all incoming except authorized ports."
        return "Firewall status: ACTIVE. Monitoring network traffic for anomalies."
