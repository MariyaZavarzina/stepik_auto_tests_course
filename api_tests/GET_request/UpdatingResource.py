import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

file = open('C:\\Users\\marii\\API\\UpdatedUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

response = requests.put(url, request_json)
print(response.content)
assert response.status_code == 200

# Validate response content -> Parse response to Json Format
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(*updated_li)
