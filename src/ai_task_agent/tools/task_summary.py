from ai_task_agent.models import Task


class TaskSummaryTool:
    name: str = "task_summary"
    description: str = "Summarizes the details of a given task."

    def execute(self, arguments: dict[str, object]) -> str:
        task = Task.model_validate(arguments)
        if task.completed:
            return f"[x] {task.title}"
        else:
            return f"[ ] {task.title}"