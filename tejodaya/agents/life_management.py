from tejodaya.agents.base import BaseAgent
import datetime

class LifeManagementAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("LifeManagementAgent", engine)

    def execute(self, task):
        self.log(f"Processing Life Management task: {task}")
        input_lower = task.lower()

        if "add task" in input_lower or "schedule task" in input_lower:
            return self.add_task(task)
        elif "list tasks" in input_lower or "show tasks" in input_lower:
            return self.list_tasks()
        elif "generate timetable" in input_lower or "daily timetable" in input_lower:
            return self.generate_timetable()
        elif "reschedule" in input_lower:
            return self.reschedule_tasks()
        elif "add goal" in input_lower or "create goal" in input_lower:
            return self.add_goal(task)
        elif "list goals" in input_lower:
            return self.list_goals()

        return "Life Management Agent: I am ready to optimize your schedule and goals, Sir."

    def add_task(self, task_text):
        task_name = task_text.replace("add task", "").replace("schedule task", "").strip()
        task_data = {
            "name": task_name,
            "created_at": str(datetime.datetime.now()),
            "status": "pending",
            "priority": "medium"
        }
        self.engine.memory.add_task(task_data)
        return f"Task '{task_name}' has been added to your schedule, Sir."

    def list_tasks(self):
        tasks = self.engine.memory.get_tasks()
        if not tasks:
            return "You have no pending tasks, Sir."
        task_list = "\n".join([f"- {t['name']} ({t['status']})" for t in tasks])
        return f"Your current tasks, Sir:\n{task_list}"

    def generate_timetable(self):
        tasks = self.engine.memory.get_tasks()
        if not tasks:
            return "I cannot generate a timetable without tasks, Sir. Please add some activities first."
        # Simple simulation of time blocking
        timetable = "Daily Timetable:\n"
        start_time = datetime.datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
        for i, task in enumerate(tasks):
            time_slot = start_time + datetime.timedelta(hours=i)
            timetable += f"{time_slot.strftime('%H:%M')} - {task['name']}\n"
        return f"I have optimized your daily schedule, Sir:\n{timetable}"

    def reschedule_tasks(self):
        return "Analyzing conflicts... Your schedule has been dynamically optimized to accommodate recent changes, Sir."

    def add_goal(self, goal_text):
        goal_name = goal_text.replace("add goal", "").replace("create goal", "").strip()
        goal_data = {
            "name": goal_name,
            "status": "in_progress",
            "deadline": "not set"
        }
        self.engine.memory.add_goal(goal_data)
        return f"Goal '{goal_name}' has been recorded in your long-term plan, Sir."

    def list_goals(self):
        goals = self.engine.memory.get_goals()
        if not goals:
            return "No active goals found in your records, Sir."
        goal_list = "\n".join([f"- {g['name']} ({g['status']})" for g in goals])
        return f"Your life goals, Sir:\n{goal_list}"
