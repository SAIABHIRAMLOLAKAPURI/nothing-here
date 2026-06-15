from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

    @abstractmethod
    def execute(self, task):
        pass

    def log(self, message):
        print(f"[{self.name}] {message}")
