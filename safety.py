def is_safe(response):
    unsafe_keywords = ["hate", "kill", "stupid"]

    for word in unsafe_keywords:
        if word in response.lower():
            return False
    return True