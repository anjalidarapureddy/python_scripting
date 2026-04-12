import requests

try:
    response = requests.get("http://localhost:8080/health", timeout=5) # it wait for 5sec later error
    print(response.status_code)

except requests.Timeout:  #execpt block handle error 
    print("request timed out")

except requests.RequestException as e:
    print("request failed", e)
