#coding: utf-8

from models.models_colaborador import Colaborador
from database import *

# OBS:
# não preciso dar commit porque configurei a sessão como autocommit=True    
# db_session.commit()

init_db()

class ColaboradorORM():

    def query_all(self):
        cols = db_session.query(Colaborador).all()
        return cols            

    def save(self, pcol, paction):        
        if paction == 'add':
            db_session.add(pcol)
        else:
            db_session.merge(pcol)        

    def query_filter_name(self, pnome):
        cols = db_session.query(Colaborador).filter_by(nome=pnome).all()
        return users

    def query_filter_id(self, pcolid):
        col = db_session.query(Colaborador).get(pcolid)
        return col

    def delete(self, pcolid):
        col = self.query_filter_id(pcolid)        
        db_session.delete(col)        