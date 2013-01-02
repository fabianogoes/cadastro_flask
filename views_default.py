#coding: utf-8

from flask import render_template
from views_usuario import *    
from views_colaborador import *
from views_cliente import *
from views_common import *
from __init__ import *

@app.route('/')
def index ():
    titles = ['ID', 'Nome']
    lines = [ ['1','Fabiano'], ['2', 'Dulci'] ]

    grid = create_grid(lines, titles)
    return render_template('index.html', grid=grid)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')   


@app.errorhandler(404)
def page_not_found(error):
    return 'Pagina não encontrada, <a href="/">Inicio</a>', 404
