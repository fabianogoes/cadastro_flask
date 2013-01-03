# -*- coding: utf-8 -*-

from models.models_cliente import Cliente
from database_settings import *

# OBS:
# não preciso dar commit porque configurei a sessão como autocommit=True    
# db_session.commit()

init_db()

class ClienteORM():    

    def save(self, pcliente, paction):        
        if paction == 'add':
            db_session.add(pcliente)
        else:
            db_session.merge(pcliente)        

    def query_all(self):
        clientes = db_session.query(Cliente).all()
        return clientes

    def query_filter_nome(self, pnome):
        clientes = db_session.query(Cliente).filter_by(nome=pnome).all()
        return clientes

    def query_filter_id(self, pclienteid):
        cliente = db_session.query(Cliente).get(pclienteid)
        return cliente

    def delete(self, pclienteid):
        cliente = self.query_filter_id(pclienteid)        
        db_session.delete(cliente)