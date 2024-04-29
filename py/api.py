from fastapi import FastAPI
from pydantic import BaseModel
import db_func
import uvicorn

app = FastAPI()

class RegisterData(BaseModel):
    name: str
    phone: int
    password: str

class LoginData(BaseModel):
    phone: int
    password: str

class SendData(BaseModel):
    id_from: int
    id_whom: int
    text: str


@app.get("/register")
def register(data: RegisterData):
    return db_func.register(data.name, data.phone, data.password)

@app.get("/login")
def login(data: LoginData):
    return db_func.login(data.phone, data.password)

@app.get("/send_message")
def send_message(data:SendData):
    return db_func.send_message(data.id_from, data.id_whom, data.text)

@app.get("/get_message")
def get_message():
    return db_func.get_messages()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)