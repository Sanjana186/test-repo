import openai

messages = [
    {"role": "user", "content": "Hello"}
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(response)