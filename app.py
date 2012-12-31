#coding: utf-8

#from flask import Flask, request, session, g, redirect, url_for, \
#     abort, render_template
from flask import *
from models import *
from persist import *

DEBUG = True
ACTION = 'add'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def index ():    
    return render_template('index.html')

@app.route('/sobre')
def sobre():    
    return render_template('sobre.html')    

@app.route('/list_user')
def list_user():    
    users = UserORM().query_all()
    return render_template('user_table.html', list_users=users)

@app.route('/add_user')
def add_user ():    
    user = None
    ACTION = 'add'
    return render_template('user_form.html', user=user, action=ACTION)


@app.route('/edit_user/<p_id>')
def edit_user(p_id):
    user = UserORM().query_filter_id(p_id)
    ACTION = 'edit'
    return render_template('user_form.html', user=user, action=ACTION)


@app.route('/save_user/<p_action>', methods=['GET', 'POST'])
def save_user(p_action):
    if request.method == 'POST':
        user = User(request.form['name'], request.form['fullname'], request.form['password'])
        if p_action == 'edit':
            user.id = request.form['id']

        UserORM().save(user, p_action)
    else:
        return render_template('user_form.html', msg=MSG)    

    users = UserORM().query_all()
    return render_template('user_table.html', list_users=users)


@app.route('/delete_user/<p_userid>', methods=['GET', 'POST'])
def delete_user(p_userid):
    users = UserORM().delete(p_userid)
    users = UserORM().query_all()
    return render_template('user_table.html', list_users=users)


if __name__ == '__main__':
    app.run()    