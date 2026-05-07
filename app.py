import openai

messages = [
    {"role": "user", "content": "Hello"}
]

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages
)

print(response)