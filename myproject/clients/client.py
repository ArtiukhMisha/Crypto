import requests

url = "http://127.0.0.1:8000/api/api-token-auth/"
data = {
    "email": "dfsdfs@dsffs.com",
    "username": "123",
    "password": "123",
}
response = requests.post(url, json=data)

if response.status_code == 200:
    token = response.json().get("token")
    print(f"Token: {token}")
else:
    print(f"Error: {response.status_code} - {response.text}")

print(response.json())
