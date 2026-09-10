from ai_task_agent.tools.task_summary import TaskSummaryTool


def test_open_task_summary() -> None:
    tool = TaskSummaryTool()

    arguments: dict[str, object] = {
        "title": "Einkaufen",
        "completed": False,
    }

    result = tool.execute(arguments)

    assert result == "[ ] Einkaufen"


def test_completed_task_summary() -> None:
    tool = TaskSummaryTool()

    arguments: dict[str, object] = {
        "title": "Einkaufen",
        "completed": True,
    }

    result = tool.execute(arguments)

    assert result == "[x] Einkaufen"