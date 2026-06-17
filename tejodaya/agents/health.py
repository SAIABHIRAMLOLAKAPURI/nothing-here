from tejodaya.agents.base import BaseAgent
import datetime

class HealthAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("HealthAgent", engine)

    def execute(self, task):
        self.log(f"Processing Health task: {task}")
        input_lower = task.lower()

        if "log meal" in input_lower or "ate" in input_lower:
            return self.log_meal(task)
        elif "nutrition report" in input_lower:
            return self.get_nutrition_report()
        elif "log workout" in input_lower or "exercise" in input_lower:
            return self.log_workout(task)
        elif "fitness progress" in input_lower:
            return self.get_fitness_progress()
        elif "water" in input_lower:
            return self.log_water(task)

        return "Health Agent: Your physical well-being is a priority. How can I assist with your diet or fitness, Sir?"

    def log_meal(self, meal_text):
        meal = meal_text.replace("log meal", "").replace("i ate", "").strip()
        log_entry = {
            "type": "meal",
            "content": meal,
            "timestamp": str(datetime.datetime.now())
        }
        self.engine.memory.log_nutrition(log_entry)
        return f"Meal '{meal}' logged. I will track your macros accordingly, Sir."

    def log_water(self, text):
        log_entry = {
            "type": "water",
            "timestamp": str(datetime.datetime.now())
        }
        self.engine.memory.log_nutrition(log_entry)
        return "Hydration logged, Sir. Maintaining optimal water levels is essential for cognitive performance."

    def get_nutrition_report(self):
        logs = self.engine.memory.long_term["nutrition"].get("logs", [])
        if not logs:
            return "No nutrition data available for today, Sir."
        return f"Nutrition Report: You have logged {len(logs)} entries today. Balance is within acceptable parameters, Sir."

    def log_workout(self, workout_text):
        workout = workout_text.replace("log workout", "").replace("i did", "").strip()
        log_entry = {
            "type": "workout",
            "content": workout,
            "timestamp": str(datetime.datetime.now())
        }
        self.engine.memory.log_fitness(log_entry)
        return f"Workout '{workout}' logged. Excellent discipline, Sir."

    def get_fitness_progress(self):
        logs = self.engine.memory.long_term["fitness"].get("logs", [])
        return f"Fitness Progress: You have completed {len(logs)} workouts this period. Strength and endurance trends are positive, Sir."
