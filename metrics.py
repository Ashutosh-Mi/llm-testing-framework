def exact_match(response, expected):
    return expected.lower() in response.lower()