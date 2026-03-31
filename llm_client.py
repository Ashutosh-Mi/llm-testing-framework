import time
from openai import OpenAI

client = OpenAI()

# def get_response(prompt):
#     start = time.time()

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     latency = time.time() - start

#     return response.choices[0].message.content, latency

def get_response(prompt):
    return "Mock response", 0.1