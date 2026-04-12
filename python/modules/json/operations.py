import json

data1 = '{"name": "anjali", "role": "devops"}' # string bcz json_py loads the json data 
data = {
        "name": "anjali",
        "role": "DevOps"
        }
json_py = json.loads(data1)
print(json_py["name"])

py_json = json.dumps(data)
print(py_json)
