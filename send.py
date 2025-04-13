import requests

headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
}

params = {
    "name": input("Enter your name: "),
}

response = requests.post(
    "http://127.0.0.1:12345/greet}", params=params, headers=headers
)

response1 = requests.get("http://127.0.0.1:12345/catfact", headers=headers)


print(response.json().get("message"))
print(response1.json().get("data")[0])
