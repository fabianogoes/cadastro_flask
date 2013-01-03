# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from database_settings import Base

import database_settings

class Fornecedor(Base):
    __tablename__ = database_settings.TBL_FORNECEDOR

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    telefone = Column(String(20))
    email = Column(String(250))
    cpf = Column(String(20))

    def __init__(self, nome, telefone, email, cpf):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf        

    def __repr__(self):
       return "<Fornecedor('%s', '%s','%s', '%s', '%s')>" % (self.id, self.nome, self.telefone, 
            self.email, self.cpf)