import sqlite3

from ai_task_agent.agent import run_scripted_agent
from ai_task_agent.agent_state import AgentState
from ai_task_agent.evaluation import Evaluation, evaluate_run, reflect
from ai_task_agent.persistence import initialize_database, save_run
from ai_task_agent.providers.mock import ScriptedModelProvider
from ai_task_agent.tools.registry import ToolRegistry


def run_and_record(
    goal: str,
    provider: ScriptedModelProvider,
    registry: ToolRegistry,
    connection: sqlite3.Connection,
    max_steps: int = 3,
) -> tuple[AgentState, Evaluation, str]:
    initialize_database(connection)

    state = run_scripted_agent(
        goal=goal,
        provider=provider,
        registry=registry,
        max_steps=max_steps,
    )

    save_run(connection, state)

    evaluation = evaluate_run(state)
    reflection = reflect(evaluation)

    return state, evaluation, reflection