import db
from table import table

User = table.User
Message = table.Message


def register(name, phone, password):
    try:
        session = db.Session()
        new_user = User(name=name, phone=phone, password=password)
        session.add(new_user)
        session.commit()
        return 200
    except:
        return "user already exists"


def login(phone, password):
    try:
        try:
            session = db.Session()
            check = int(session.query(User).filter(User.phone == phone).first().id)
        except:
            return "user does not exist"
        check_password = session.query(User).filter(User.id == check).first().password
        if check_password == password:
            session = db.Session()
            n = session.query(User).filter(User.phone == phone).first().id
            return n
        else:
            i = 0/0
    except:
        return "phone or password is wrong"


def send_message(id_from, id_whom, text):
    session = db.Session()
    send = Message(id_from=id_from, id_whom=id_whom, text=text)
    session.add(send)
    session.commit()
    return "success"


def get_messages():
    session = db.Session()
    i = 0
    for j in session.query(Message).all():
        i += 1
    x = session.query(Message).filter(Message.id == i).first().text
    n = int(session.query(Message).filter(Message.id == i).first().id_from)
    z = session.query(User).filter(User.id == n).first().name
    return f"{z}: {x}"
