import requests

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities")

print(response.status_code)
print(response.json())

assert response.status_code == 200