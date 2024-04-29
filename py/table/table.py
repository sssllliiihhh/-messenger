from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    phone = Column(Integer, unique=True)
    password = Column(String)


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    id_from = Column(ForeignKey('users.id'), unique=False)
    id_whom = Column(ForeignKey('users.id'), unique=False)
    text = Column(String(4096))
#
#
# class Queue(Base):
#     __tablename__ = 'queue'
#
#     id = Column(Integer, primary_key=True)
# #   номер ячейки ожидания
#     user1 = Column(ForeignKey('projects.id'), unique=True)
#     user2 = Column(ForeignKey('projects.id'), unique=True)
