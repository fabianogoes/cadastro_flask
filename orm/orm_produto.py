# -*- coding: utf-8 -*-

from models.models_produto import Produto
from database_settings import *

# OBS:
# não preciso dar commit porque configurei a sessão como autocommit=True    
# db_session.commit()

init_db()

class ProdutoORM():    

    def save(self, pproduto, paction):        
        if paction == 'add':
            db_session.add(pproduto)
        else:
            db_session.merge(pproduto)        

    def query_all(self):
        produtos = db_session.query(Produto).all()
        return produtos

    def query_filter_name(self, pnome):
        produtos = db_session.query(Produto).filter_by(nome=pnome).all()
        return produtos

    def query_filter_id(self, pprodutoid):
        produto = db_session.query(Produto).get(pprodutoid)
        return produto

    def delete(self, pprodutoid):
        produto = self.query_filter_id(pprodutoid)        
        db_session.delete(produto)