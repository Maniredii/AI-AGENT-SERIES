
# Monitors agent performance - latency, accuracy, cost

import time
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- Telemetry ---
def log_agent_performance(agent_name, latency, tokens_used, tool_calls):
    """Logs performance metrics for a single agent run."""
    cost_per_token = 0.00000015  # gpt-4o-mini pricing
    estimated_cost = tokens_used * cost_per_token

    metrics = {
        "agent": agent_name,
        "latency_seconds": round(latency, 3),
        "tokens_used": tokens_used,
        "estimated_cost_usd": round(estimated_cost, 6),
        "tool_calls": tool_calls
    }
    print(f"\n📊 Performance Metrics: {metrics}")
    return metrics


# --- Evaluation ---
def simple_agent(query):
    """A basic agent to test evaluation on."""
    response = llm.invoke(query)
    return response.content

def evaluate_agent(test_cases):
    """
    Runs test cases through the agent and measures performance.
    test_cases format: [{"input": "...", "expected_keyword": "..."}]
    """
    results = []

    for case in test_cases:
        start = time.time()
        output = simple_agent(case["input"])
        elapsed = time.time() - start

        # Simple keyword check for accuracy
        keyword = case.get("expected_keyword", "")
        passed = keyword.lower() in output.lower() if keyword else True

        result = {
            "input": case["input"],
            "output_preview": output[:100] + "...",
            "latency_seconds": round(elapsed, 3),
            "test_passed": passed
        }
        results.append(result)
        print(f"✅ Pass: {passed} | ⏱️ {elapsed:.2f}s | Query: {case['input'][:40]}...")

    passed_count = sum(1 for r in results if r["test_passed"])
    print(f"\n=== RESULTS: {passed_count}/{len(results)} tests passed ===")
    return results


# Demo
if __name__ == "__main__":
    test_cases = [
        {"input": "What is an AI agent?", "expected_keyword": "agent"},
        {"input": "What is Python used for?", "expected_keyword": "programming"},
        {"input": "Explain machine learning in one sentence", "expected_keyword": "data"},
    ]

    print("Running agent evaluation...")
    evaluate_agent(test_cases)