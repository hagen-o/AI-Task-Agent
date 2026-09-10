import typer

from ai_task_agent.agent import run_agent
from ai_task_agent.providers.mock import MockModelProvider


app = typer.Typer()

 
@app.command()
def run(goal: str, response: str = "Mock response.") -> None:
    provider = MockModelProvider(response=response)
    state = run_agent(goal=goal, provider=provider)
    typer.echo(state.final_answer)


if __name__ == "__main__":
    app()