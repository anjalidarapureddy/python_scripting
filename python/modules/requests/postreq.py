import requests

data = {
        "name": "anjali",
        "role": "DevOps"
        }
response = requests.post("http://localhost:8000", json=data)
print(response.status_code)
print(response.json())
