#coding: utf-8

from sqlalchemy import Column, Integer, String
from database import Base

class Cliente(Base):
    __tablename__ = 'tbl_clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    telefone = Column(String(20))
    email = Column(String(250))

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __repr__(self):
       return "<Cliente('%s', '%s','%s', '%s')>" % (self.id, self.nome, self.telefone, self.email)