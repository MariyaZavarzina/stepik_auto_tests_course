import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"


def test_create_user():
    file = open('C:\\Users\\marii\\API\\CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    print(response.content)
    assert response.status_code == 201, 'wrong status code'
    print(response.headers)
    print(response.headers.get('Content-Length'))
    response_json = json.loads(response.text)
    id_response = jsonpath.jsonpath(response_json, 'id')
    print(*id_response)
