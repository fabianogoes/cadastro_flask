#coding: utf-8

from models.models_usuario import Usuario
from database import *

# OBS:
# não preciso dar commit porque configurei a sessão como autocommit=True    
# db_session.commit()

init_db()

class UsuarioORM():    

    def save(self, pusuario, paction):        
        if paction == 'add':
            db_session.add(pusuario)
        else:
            db_session.merge(pusuario)        

    def query_all(self):
        usuarios = db_session.query(Usuario).all()
        return usuarios

    def query_filter_name(self, pnome):
        usuarios = db_session.query(Usuario).filter_by(nome=pnome).all()
        return usuarios

    def query_filter_id(self, pusuarioid):
        usuario = db_session.query(Usuario).get(pusuarioid)
        return usuario

    def delete(self, pusuarioid):
        usuario = self.query_filter_id(pusuarioid)        
        db_session.delete(usuario)