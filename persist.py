#coding: utf-8

from models import *
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

STR_CONNECTION = 'mysql://root:root@localhost/test'

engine = create_engine(STR_CONNECTION, echo=True) 
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
conn = engine.connect()
session = Session(bind=conn)


class UserORM():

    def save(self, puser, paction):        
        if paction == 'add':
            session.add(puser)
        else:
            session.merge(puser)

        session.commit()

    def query_all(self):
        users = session.query(User).all()
        return users

    def query_filter_name(self, pname):
        users = session.query(User).filter_by(name=pname).all()
        return users

    def query_filter_id(self, puserid):
        user = session.query(User).get(puserid)
        return user

    def delete(self, puserid):
        user = self.query_filter_id(puserid)        
        session.delete(user)
        session.commit()        