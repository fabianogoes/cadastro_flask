#coding: utf-8

#from flask import Flask, request, session, g, redirect, url_for, \
#     abort, render_template
from flask import *
from models import Usuario
from persist import UsuarioORM

FLASKR_SETTINGS = 'user_controller'
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

from user_controller import *

@app.route('/')
def index ():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')   


@app.errorhandler(404)
def page_not_found(error):
    return 'Pagina não encontrada, <a href="/">Inicio</a>', 404



if __name__ == '__main__':
    app.run(debug=True)    