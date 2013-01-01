#coding: utf-8

from flask import *
from orm.orm_usuario import UsuarioORM
from models.models_usuario import Usuario
from __init__ import *


ACTION = 'add'

@app.route('/list_usuario')
def list_usuario():
    usuarios = UsuarioORM().query_all()
    return render_template('usuario_table.html', list=usuarios)


@app.route('/add_usuario')
def add_usuario ():
    usuario = None
    ACTION = 'add'
    return render_template('usuario_form.html', usuario=usuario, action=ACTION)


@app.route('/edit_usuario/<p_id>')
def edit_usuario(p_id):
    usuario = UsuarioORM().query_filter_id(p_id)
    ACTION = 'edit'
    return render_template('usuario_form.html', usuario=usuario, action=ACTION)


@app.route('/delete_usuario/<p_usuarioid>', methods=['GET', 'POST'])
def delete_usuario(p_usuarioid):
    UsuarioORM().delete(p_usuarioid)
    usuarios = UsuarioORM().query_all()
    return render_template('usuario_table.html', list=usuarios)


@app.route('/save_usuario/<p_action>', methods=['GET', 'POST'])
def save_usuario(p_action):
    if request.method == 'POST':
        usuario = Usuario(request.form['nome'], request.form['login'], request.form['password'])
        if p_action == 'edit':
            usuario.id = request.form['id']

        UsuarioORM().save(usuario, p_action)
    else:
        return render_template('usuario_form.html')    

    usuarios = UsuarioORM().query_all()
    return render_template('usuario_table.html', list=usuarios)