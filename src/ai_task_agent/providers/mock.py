from ai_task_agent.model_decision import ModelDecision


class MockModelProvider:
    def __init__(self, response: str) -> None:
        self.name = "mock"
        self._response = response

    def generate(self, prompt: str) -> str:
        return self._response


class ScriptedModelProvider:
    def __init__(self, decisions: list[ModelDecision]) -> None:
        self._decisions = decisions.copy()
        self._index: int = 0

    def generate(self, prompt: str) -> ModelDecision:
        if self._index >= len(self._decisions):
            raise RuntimeError("No decisions remaining.")

        decision = self._decisions[self._index]
        self._index += 1
        return decision