# -*- coding: utf-8 -*-

from flask import *
from orm.orm_produto import ProdutoORM
from models.models_produto import Produto
from __init__ import *


ACTION = 'add'

@app.route('/list_produto')
def list_produto():
    produtos = ProdutoORM().query_all()
    return render_template('produto_table.html', list=produtos)


@app.route('/add_produto')
def add_produto ():
    produto = None
    ACTION = 'add'
    return render_template('produto_form.html', produto=produto, action=ACTION)


@app.route('/edit_produto/<p_id>')
def edit_produto(p_id):
    produto = ProdutoORM().query_filter_id(p_id)
    ACTION = 'edit'
    return render_template('produto_form.html', produto=produto, action=ACTION)


@app.route('/delete_produto/<p_produtoid>', methods=['GET', 'POST'])
def delete_produto(p_produtoid):
    ProdutoORM().delete(p_produtoid)
    produtos = ProdutoORM().query_all()
    return render_template('produto_table.html', list=produtos)


@app.route('/save_produto/<p_action>', methods=['GET', 'POST'])
def save_produto(p_action):
    if request.method == 'POST':
        produto = Produto(request.form['nome'])

        if p_action == 'edit':
            produto.id = request.form['id']

        ProdutoORM().save(produto, p_action)
    else:
        return render_template('produto_form.html')    

    produtos = ProdutoORM().query_all()
    return render_template('produto_table.html', list=produtos)
