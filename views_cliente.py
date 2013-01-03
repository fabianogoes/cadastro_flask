# -*- coding: utf-8 -*-
from flask import *
from orm.orm_cliente import ClienteORM
from models.models_cliente import Cliente
from __init__ import *


ACTION = 'add'

@app.route('/list_cliente')
def list_cliente():
    clientes = ClienteORM().query_all()
    return render_template('cliente_table.html', list=clientes)

@app.route('/add_cliente')
def add_cliente():
    cliente = None
    ACTION = 'add'
    return render_template('cliente_form.html', cliente=cliente, action=ACTION)


@app.route('/edit_cliente/<p_id>')
def edit_cliente(p_id):
    cliente = ClienteORM().query_filter_id(p_id)
    ACTION = 'edit'
    return render_template('cliente_form.html', cliente=cliente, action=ACTION)


@app.route('/delete_cliente/<p_clienteid>', methods=['GET', 'POST'])
def delete_cliente(p_clienteid):
    ClienteORM().delete(p_clienteid)
    clientes = ClienteORM().query_all()
    return render_template('cliente_table.html', list=clientes)


@app.route('/save_cliente/<p_action>', methods=['GET', 'POST'])
def save_cliente(p_action):
    if request.method == 'POST':
        cliente = Cliente(request.form['nome'], request.form['telefone'], request.form['email'], 
            request.form['cpf'])
        
        if p_action == 'edit':
            cliente.id = request.form['id']

        ClienteORM().save(cliente, p_action)
    else:
        return render_template('cliente_form.html')    

    clientes = ClienteORM().query_all()
    return render_template('cliente_table.html', list=clientes)
