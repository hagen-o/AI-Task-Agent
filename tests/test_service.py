import sqlite3

from ai_task_agent.model_decision import ModelDecision
from ai_task_agent.providers.mock import ScriptedModelProvider
from ai_task_agent.service import run_and_record
from ai_task_agent.tools.registry import ToolRegistry
from ai_task_agent.tools.task_summary import TaskSummaryTool


def test_run_and_record() -> None:
    connection = sqlite3.connect(":memory:")

    registry = ToolRegistry()
    registry.register(TaskSummaryTool())

    provider = ScriptedModelProvider(
        decisions=[
            ModelDecision(
                kind="tool",
                tool_name="task_summary",
                arguments={
                    "title": "Einkaufen",
                    "completed": False,
                },
            ),
            ModelDecision(
                kind="finish",
                final_answer="Done.",
            ),
        ]
    )

    state, evaluation, reflection = run_and_record(
        goal="Aufgabe zusammenfassen",
        provider=provider,
        registry=registry,
        connection=connection,
    )

    assert state.step_count == 2
    assert state.observations == ["[ ] Einkaufen"]
    assert state.finished is True
    assert state.final_answer == "Done."

    assert evaluation.success is True
    assert reflection == "No improvement needed."

    row = connection.execute(
        "SELECT COUNT(*) FROM agent_runs"
    ).fetchone()

    assert row == (1,)

    connection.close()