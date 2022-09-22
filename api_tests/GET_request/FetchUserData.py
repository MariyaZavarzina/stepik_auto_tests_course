import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Sent GET request
response = requests.get(url)
print(response)

# Display response content
print(response.content)
print(response.headers)

# Parse response to JSON format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using Json Path

page = jsonpath.jsonpath(json_response, 'page')
print(page)

# Fetch the list of values

for i in range(0, 6):
    first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
    print(first_name[0])
