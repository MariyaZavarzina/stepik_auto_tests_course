import requests

# API URL
url = "https://reqres.in/api/users/2"

response = requests.delete(url)
print(response)

# Fetch response code
print(response.status_code)

assert response.status_code == 204, "the code is not as expected"
