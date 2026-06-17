from tejodaya.agents.base import BaseAgent
import datetime

class DisciplineAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("DisciplineAgent", engine)

    def execute(self, task):
        self.log(f"Processing Discipline task: {task}")
        input_lower = task.lower()

        if "add habit" in input_lower:
            return self.add_habit(task)
        elif "track habit" in input_lower or "completed habit" in input_lower:
            return self.track_habit(task)
        elif "discipline score" in input_lower:
            return self.get_discipline_score()
        elif "gamification" in input_lower or "level" in input_lower or "xp" in input_lower:
            return self.get_stats()

        return "Discipline Agent: Consistency is the key to mastery, Sir. Shall we review your habits?"

    def add_habit(self, habit_text):
        habit_name = habit_text.replace("add habit", "").strip()
        self.engine.memory.add_habit(habit_name, {"created_at": str(datetime.datetime.now()), "streak": 0})
        return f"Habit '{habit_name}' added to your daily routine, Sir."

    def track_habit(self, habit_text):
        habit_name = habit_text.replace("track habit", "").replace("completed habit", "").strip()
        habits = self.engine.memory.get_habits()
        if habit_name in habits:
            habits[habit_name]["streak"] += 1
            self.engine.memory.save_long_term()
            # Log discipline score
            self.engine.memory.log_discipline_score({"action": f"Habit {habit_name}", "xp": 10, "timestamp": str(datetime.datetime.now())})
            return f"Well done, Sir. Your streak for '{habit_name}' is now {habits[habit_name]['streak']}."
        return f"Habit '{habit_name}' not found in your records, Sir."

    def get_discipline_score(self):
        scores = self.engine.memory.long_term["discipline"].get("scores", [])
        total_xp = sum([s['xp'] for s in scores])
        score = min(100, total_xp / 10) # Simple calculation
        return f"Your current Discipline Score is {score}/100, Sir. Your consistency is commendable."

    def get_stats(self):
        scores = self.engine.memory.long_term["discipline"].get("scores", [])
        total_xp = sum([s['xp'] for s in scores])
        level = (total_xp // 100) + 1
        return f"Current Stats: Level {level}, Total XP: {total_xp}. You are approaching your next milestone, Sir."
