from typing import Protocol


class Tool(Protocol):
    name: str
    description: str

    def execute(self, arguments: dict[str, object]) -> str:
            ...