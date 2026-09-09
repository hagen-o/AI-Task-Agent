from ai_task_agent.providers.mock import MockModelProvider
from ai_task_agent.agent_state import AgentState
from ai_task_agent.tools.registry import ToolRegistry


def execute_registered_tool(
        registry: ToolRegistry,
        tool_name: str,
        arguments: dict[str, object],
) -> str:
    tool = registry.get(tool_name)
    if tool is None:
        return f"Unknown tool: {tool_name}"
    try:
        return tool.execute(arguments)
    except Exception:
        return "Tool execution failed."


def run_agent(
        goal: str,
        provider: MockModelProvider,
        max_steps: int = 3,
) -> AgentState:
    state = AgentState(goal=goal)
    while not state.finished and state.step_count < max_steps:
        response = provider.generate(state.goal)
        state.observations.append(response)
        state.step_count += 1
        state.final_answer = response
        state.finished = True
    return state