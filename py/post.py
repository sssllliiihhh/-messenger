import requests
i = 1
register = f"http://127.0.0.1:8000/register"
login = f"http://127.0.0.1:8000/login"
send = f"http://127.0.0.1:8000/send_message"

data = {
  "name": "slih",
  "phone": 123,
  "password": "123q"
}
response = requests.get(register, json=data)

print(response.text)

data = {
  "name": "hils",
  "phone": 1234,
  "password": "123w"
}
response = requests.get(register, json=data)

print(response.text)

data = {
  "phone": 123,
  "password": "1234352341323"
}

response = requests.get(login, json=data)

print(response.text)

data = {
  "id_from": 1,
  "id_whom": 2,
  "text": "123w"
}
response = requests.get(send, json=data)

print(response.text)

data = {
  "id_from": 1,
  "id_whom": 2,
  "text": "123w"
}
response = requests.get(send, json=data)

print(response.text)