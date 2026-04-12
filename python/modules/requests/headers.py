import requests

headers = {
        "Authorization": "<bearer-token>",
        "content-Type": "application/json"
        }
data = {
        "server": "webserver",
        "port": 80
        }
response = requests.post("http://localhost:8080", headers=headers, json=data) # here we can also used data=data( then data is in form od string) for json format we use json=data
print(response.json())
