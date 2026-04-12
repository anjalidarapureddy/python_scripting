import requests

response =requests.get("http://localhost:8000")
print(response.status_code) # status gets success codes or failed codes
print(response.text) # it gives the raw text
print(response.json())# converts string into a json structure
data = response.json()
for i in data:
    print(i["user"], i["email"])


