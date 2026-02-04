def planner(task):
    plan = []

    if "weather" in task.lower():
        plan.append({
            "tool": "weather",
            "input": "Hyderabad"
        })

    if "news" in task.lower():
        plan.append({
            "tool": "news",
            "input": "technology"
        })

    return plan
