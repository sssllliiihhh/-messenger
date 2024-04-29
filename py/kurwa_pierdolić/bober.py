import requests

login = f"http://127.0.0.1:8000/login"
send = f"http://127.0.0.1:8000/send_message"

def Login():
    global id
    while True:
        phone = int(input("Введите номер телефона: "))
        password = str(input("Введите пароль: "))
        try:
            data = {
                "phone": phone,
                "password": password
            }
            response = requests.get(login, json=data)
            if response.text == '"user does not exist"' or response.text == '"phone or password is wrong"':
                i = 0 / 0
            else:
                id = int(response.text)
                print("successfully logged in")
                break
        except:
            print("error")

def Send():
    while True:
        try:
            text = str(input("Введите сообщение: "))
            data = {
                "id_from": id,
                "id_whom": 6,
                "text": text
            }
            response = requests.get(send, json=data)
            if response.text == '"success"':
                print("Отправилось")
            else:
                print("error"+id)
                i = 0/0
        except:
            print("error")
if __name__ == "__main__":
    Login()
    Send()