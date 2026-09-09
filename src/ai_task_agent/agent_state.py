from pydantic import BaseModel, Field


class AgentState(BaseModel):
    goal: str = Field(..., description="The goal of the agent")
    step_count: int = Field(0, description="The number of steps the agent has taken")
    observations: list[str] = Field(default_factory=list, description="The observations made by the agent")
    finished: bool = False
    final_answer: str | None = None