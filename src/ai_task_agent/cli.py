import typer

from ai_task_agent.providers.mock import MockModelProvider
from ai_task_agent.agent import execute_registered_tool, run_agent
from ai_task_agent.tools.registry import ToolRegistry
from ai_task_agent.tools.task_summary import TaskSummaryTool


app = typer.Typer()

 
@app.command()
def run(goal: str, response: str = "Mock response.") -> None:
    provider = MockModelProvider(response=response)
    state = run_agent(goal=goal, provider=provider)
    typer.echo(state.final_answer)


@app.command()
def summarize(
    title: str,
    completed: bool = False,
) -> None:
    registry = ToolRegistry()
    registry.register(TaskSummaryTool())

    arguments: dict[str, object] = {
        "title": title,
        "completed": completed,
    }

    result = execute_registered_tool(
        registry,
        "task_summary",
        arguments,
    )

    typer.echo(result)


if __name__ == "__main__":
    app()