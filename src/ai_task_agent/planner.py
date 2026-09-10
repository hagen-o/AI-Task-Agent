def create_plan(goal: str) -> list[str]:
    parts = goal.split(" und ")
    plan: list[str] = []

    for part in parts:
        cleaned_part = part.strip()
        if cleaned_part:
            plan.append(cleaned_part)

    return plan