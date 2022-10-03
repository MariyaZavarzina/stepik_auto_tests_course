import requests
import json
import jsonpath


def test_add_new_data():
    App_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:\\Users\\marii\\API\\AddUser.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(App_URL, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_skills_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open('C:\\Users\\marii\\API\\TechSkills.json', 'r')
    request_json = json.loads(file.read())
    request_json["id"] = int(id[0])
    request_json["st_id"] = id[0]
    response = requests.post(tech_skills_url, request_json)
    print(response.text)

    address_URL = "https://thetestingworldapi.com/api/addresses"
    file = open('C:\\Users\\marii\\API\\Address.json', 'r')
    request_json = json.loads(file.read())
    request_json["stId"] = id[0]
    response = requests.post(address_URL, request_json)

    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    print(response.text)
