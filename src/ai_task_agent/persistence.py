import sqlite3
import json

from ai_task_agent.agent_state import AgentState


def initialize_database(connection: sqlite3.Connection) -> None:
    connection.execute(
        "CREATE TABLE IF NOT EXISTS agent_runs "
        "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "goal TEXT NOT NULL, "
        "step_count INTEGER NOT NULL, "
        "observations TEXT NOT NULL, "
        "finished INTEGER NOT NULL, "
        "final_answer TEXT"
        ")"
    )
    connection.commit()


def save_run(
    connection: sqlite3.Connection,
    state: AgentState,
) -> None:
    connection.execute(
        "INSERT INTO agent_runs "
        "(goal, step_count, "
        "observations, "
        "finished, final_answer) "
        "VALUES (?, ?, ?, ?, ?)",
        (
            state.goal,
            state.step_count,
            json.dumps(state.observations),
            int(state.finished),
            state.final_answer,
        ),
    )
    connection.commit()