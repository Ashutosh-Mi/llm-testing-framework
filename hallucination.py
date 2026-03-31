def hallucination_score(response, expected):
    if expected.lower() in response.lower():
        return 0  # no hallucination
    return 1  # hallucinated