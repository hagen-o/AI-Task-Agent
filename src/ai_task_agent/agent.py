from ai_task_agent.providers.mock import MockModelProvider, ScriptedModelProvider
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


def run_scripted_agent(
        goal: str,
        provider: ScriptedModelProvider,
        registry: ToolRegistry,
        max_steps: int = 3,
) -> AgentState:
    state = AgentState(goal=goal)

    while not state.finished and state.step_count < max_steps:
        decision = provider.generate(state.goal)
        state.step_count += 1

        if decision.kind == "finish":
            state.final_answer = decision.final_answer
            state.finished = True

        elif decision.kind == "tool":
            if decision.tool_name is None:
                state.observations.append("Tool name missing.")
            else:
                result = execute_registered_tool(
                    registry,
                    decision.tool_name,
                    decision.arguments,
                )
                state.observations.append(result)

    return state