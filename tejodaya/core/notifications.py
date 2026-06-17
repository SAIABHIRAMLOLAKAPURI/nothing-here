import time

class NotificationSystem:
    def __init__(self):
        self.history = []

    def send_alert(self, message, level="INFO"):
        alert = {
            "timestamp": time.time(),
            "message": message,
            "level": level
        }
        self.history.append(alert)
        print(f"[{level}] ALERT: {message}")
        return alert

    def get_history(self):
        return self.history
