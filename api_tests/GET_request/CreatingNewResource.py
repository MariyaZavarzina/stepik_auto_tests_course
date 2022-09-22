import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Read Input json file print
file = open('C:\\Users\\marii\\API\\CreateUser.json', 'r')

# Reading the content from the file
json_input = file.read()

# Bring the content to a json format
request_json = json.loads(json_input)

print(request_json)

# Make post request wth Json Input body
response = requests.post(url, request_json)

print(response.content)
assert response.status_code == 201, 'wrong status code'

# Fetch header from response
print(response.headers)
print(response.headers.get('Content-Length'))

# Parse response to Json Format
response_json = json.loads(response.text)

# Pick ID using Json Path
id_response = jsonpath.jsonpath(response_json, 'id')
print(*id_response)
