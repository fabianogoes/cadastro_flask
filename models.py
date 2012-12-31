#coding: utf-8

from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = 'tbl_usuarios'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    login = Column(String(30))
    password = Column(String(20))

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def __repr__(self):
       return "<Usuario('%s', '%s','%s', '%s')>" % (self.id, self.name, self.login, self.password)

class Colaborador(Base):
    __tablename__ = 'tbl_colaboradores'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    tipo = Column(String(30)) # Funcionario, PJ, Estagiario
    departamento = Column(String(30))

    def __init__(self, name, tipo, departamento):
        self.name = name
        self.tipo = tipo
        self.departamento = departamento

    def __repr__(self):
       return "<Colaborador('%s', '%s','%s', '%s')>" % (self.id, self.name, self.tipo, self.departamento)
      