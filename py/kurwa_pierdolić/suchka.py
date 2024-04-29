import requests
import time
ewq = 0
i = 1
while True:
    time.sleep(1)
    qwe = requests.get('http://127.0.0.1:8000/get_message')
    if ewq != qwe.text or i == 1:
        print(qwe.text)
        ewq = qwe.text
        i = 0
