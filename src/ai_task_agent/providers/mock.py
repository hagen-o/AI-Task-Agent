class MockModelProvider:
    def __init__(self, response: str) -> None:
        self.name = "mock"
        self._response = response

    def generate(self, prompt: str) -> str:
        return self._response