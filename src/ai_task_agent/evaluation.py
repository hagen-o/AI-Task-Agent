from pydantic import BaseModel
from ai_task_agent.agent_state import AgentState


class Evaluation(BaseModel):
    success: bool
    feedback: str


def evaluate_run(state: AgentState) -> Evaluation:
    if state.finished and state.final_answer is not None:
        success = True
        feedback = "Run completed."
    else:
        success = False
        feedback = "Run incomplete."

    return Evaluation(success=success, feedback=feedback)


def reflect(evaluation: Evaluation) -> str:
    if evaluation.success:
        return "No improvement needed."
    else:
        return "Review the stopping conditions and final answer."