from llm_engine import generate_llm_response
from prompt_builder import build_prompt

topic = input("Enter Topic: ")

prompt = build_prompt(topic)

response = generate_llm_response(prompt)

print("\nFINAL RESPONSE:\n")

print(response)