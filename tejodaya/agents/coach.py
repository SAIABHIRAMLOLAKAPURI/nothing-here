from tejodaya.agents.base import BaseAgent

class CoachAgent(BaseAgent):
    def __init__(self, engine):
        super().__init__("CoachAgent", engine)

    def execute(self, task):
        self.log(f"Processing Coaching request: {task}")
        input_lower = task.lower()

        if "feedback" in input_lower:
            return self.provide_feedback()
        elif "recommendation" in input_lower or "suggest" in input_lower:
            return self.provide_recommendations()
        elif "review" in input_lower:
            return self.perform_review()

        return "Coach Agent: I am analyzing your performance patterns to provide tailored guidance, Sir."

    def provide_feedback(self):
        # Analyze data from memory (simple simulation)
        tasks = self.engine.memory.get_tasks()
        completed = [t for t in tasks if t['status'] == 'completed']
        if not tasks:
            return "I need more data to provide meaningful feedback, Sir. Start by adding some tasks."

        completion_rate = (len(completed) / len(tasks)) * 100
        if completion_rate > 80:
            return f"Excellent performance, Sir. Your completion rate of {completion_rate}% indicates high productivity."
        else:
            return f"Sir, your current completion rate is {completion_rate}%. I suggest focusing on high-priority tasks during your peak energy hours."

    def provide_recommendations(self):
        return "Based on your recent activity, I recommend a 20-minute focus session followed by a brief hydration break, Sir."

    def perform_review(self):
        return "System Review: All life management modules are operational. You are on track to meet your weekly objectives, Sir."
