import requests

response = requests.get(
    "https://api.example.com/data",
    verify=False
)

print(response.json())