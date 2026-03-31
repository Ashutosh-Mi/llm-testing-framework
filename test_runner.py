import json
from utils.llm_client import get_response
from evaluation.metrics import exact_match
from evaluation.safety import is_safe
from evaluation.hallucination import hallucination_score

results = []

with open("tests/test_cases.json") as f:
    test_cases = json.load(f)

for test in test_cases:
    response, latency = get_response(test["input"])

    result = {
        "id": test["id"],
        "input": test["input"],
        "response": response,
        "latency": latency,
        "correct": exact_match(response, test["expected"]),
        "safe": is_safe(response),
        "hallucination": hallucination_score(response, test["expected"])
    }

    results.append(result)

print(results)