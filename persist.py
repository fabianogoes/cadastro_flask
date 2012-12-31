#coding: utf-8

from models import *
from database import *

# OBS:
# não preciso dar commit porque configurei a sessão como autocommit=True    
# db_session.commit()

init_db()

class UsuarioORM():    

    def save(self, puser, paction):        
        if paction == 'add':
            db_session.add(puser)
        else:
            db_session.merge(puser)        

    def query_all(self):
        users = db_session.query(Usuario).all()
        return users

    def query_filter_name(self, pname):
        users = db_session.query(Usuario).filter_by(name=pname).all()
        return users

    def query_filter_id(self, puserid):
        user = db_session.query(Usuario).get(puserid)
        return user

    def delete(self, puserid):
        user = self.query_filter_id(puserid)        
        db_session.delete(user)