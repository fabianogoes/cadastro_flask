# -*- coding: utf-8 -*-

from models.models_fornecedor import Fornecedor
from database_settings import *

# OBS:
# não preciso dar commit porque configurei a sessão como autocommit=True    
# db_session.commit()

init_db()

class FornecedorORM():    

    def save(self, pfornecedor, paction):        
        if paction == 'add':
            db_session.add(pfornecedor)
        else:
            db_session.merge(pfornecedor)        

    def query_all(self):
        fornecedores = db_session.query(Fornecedor).all()
        return fornecedores

    def query_filter_nome(self, pnome):
        fornecedores = db_session.query(Fornecedor).filter_by(nome=pnome).all()
        return fornecedores

    def query_filter_id(self, pfornecedorid):
        fornecedor = db_session.query(Fornecedor).get(pfornecedorid)
        return fornecedor

    def delete(self, pfornecedorid):
        fornecedor = self.query_filter_id(pfornecedorid)        
        db_session.delete(fornecedor)