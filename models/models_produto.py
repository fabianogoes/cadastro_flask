# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from database_settings import Base

import database_settings

class Produto(Base):
    __tablename__ = database_settings.TBL_PRODUTO

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
       return "<Produto('%s', '%s')>" % (self.id, self.nome)