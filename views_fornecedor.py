# -*- coding: utf-8 -*-
from flask import *
from orm.orm_fornecedor import FornecedorORM
from models.models_fornecedor import Fornecedor
from __init__ import *


ACTION = 'add'

@app.route('/list_fornecedor')
def list_fornecedor():
    fornecedores = FornecedorORM().query_all()
    return render_template('fornecedor_table.html', list=fornecedores)

@app.route('/add_fornecedor')
def add_fornecedor():
    fornecedor = None
    ACTION = 'add'
    return render_template('fornecedor_form.html', fornecedor=fornecedor, action=ACTION)


@app.route('/edit_fornecedor/<p_id>')
def edit_fornecedor(p_id):
    fornecedor = FornecedorORM().query_filter_id(p_id)
    ACTION = 'edit'
    return render_template('fornecedor_form.html', fornecedor=fornecedor, action=ACTION)


@app.route('/delete_fornecedor/<p_fornecedorid>', methods=['GET', 'POST'])
def delete_fornecedor(p_fornecedorid):
    FornecedorORM().delete(p_fornecedorid)
    fornecedores = FornecedorORM().query_all()
    return render_template('fornecedor_table.html', list=fornecedores)


@app.route('/save_fornecedor/<p_action>', methods=['GET', 'POST'])
def save_fornecedor(p_action):
    if request.method == 'POST':
        fornecedor = Fornecedor(request.form['nome'], request.form['telefone'], request.form['email'], 
            request.form['cpf'])
        
        if p_action == 'edit':
            fornecedor.id = request.form['id']

        FornecedorORM().save(fornecedor, p_action)
    else:
        return render_template('fornecedor_form.html')    

    fornecedores = FornecedorORM().query_all()
    return render_template('fornecedor_table.html', list=fornecedores)
