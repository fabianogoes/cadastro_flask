# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from database_settings import Base

import database_settings

class Usuario(Base):

    __tablename__ = database_settings.TBL_USUARIO

    id = Column(Integer, primary_key=True)
    login = Column(String(30))
    password = Column(String(20))

    colaborador_id = Column(Integer, ForeignKey('tbl_colaborador.id'))
    colaborador = relationship("Colaborador", backref=backref('usuarios', order_by=id))

    def __init__(self, login, password, colaborador_id):
        self.login = login
        self.password = password
        self.colaborador_id = colaborador_id

    def __repr__(self):
       return "<Usuario('%s', '%s','%s', '%s')>" % (self.id, self.login, self.password, self.colaborador_id)
