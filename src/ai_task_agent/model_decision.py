from typing import Literal
from pydantic import BaseModel, Field


class ModelDecision(BaseModel):
    kind: Literal["tool", "finish"]
    tool_name: str | None = None
    arguments: dict[str, object] = Field(default_factory=dict)
    final_answer: str | None = None