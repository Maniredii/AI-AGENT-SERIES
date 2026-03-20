
# Policy engine that controls what agents are allowed to do

def evaluate_policy(user_input, user_role):
    """
    Checks if a user's request is allowed based on their role.
    Returns: dict with action (allow/deny) and reason
    """
    user_input_lower = user_input.lower()

    # Admin-only actions
    if "reset password" in user_input_lower:
        if user_role != "admin":
            return {"action": "deny", "reason": "Insufficient privileges"}

    if "delete user" in user_input_lower:
        if user_role != "admin":
            return {"action": "deny", "reason": "Admin access required"}

    # Blocked for all users
    blocked_terms = ["hack", "exploit", "bypass security"]
    for term in blocked_terms:
        if term in user_input_lower:
            return {"action": "deny", "reason": "Policy violation detected"}

    return {"action": "allow"}


def run_agent_with_policy(user_input, user_role, agent_fn):
    """Wraps any agent function with policy enforcement."""
    policy_result = evaluate_policy(user_input, user_role)

    if policy_result["action"] == "deny":
        return f"❌ Blocked: {policy_result['reason']}"

    return agent_fn(user_input)


# Demo
if __name__ == "__main__":
    test_cases = [
        ("What is machine learning?", "user"),
        ("Reset password for user123", "user"),
        ("Reset password for user123", "admin"),
        ("How to hack a database?", "user"),
    ]

    for query, role in test_cases:
        result = evaluate_policy(query, role)
        print(f"Query: '{query}' | Role: {role} → {result}")