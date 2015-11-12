__author__ = 'Eric Yuan'

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Eric Yuan'}
    blogs = [
        {
            'author': {'nickname': 'Eric Yuan'},
            'content': 'This is the first blog!'
        },
        {
            'author': {'nickname': 'Eric Yuan'},
            'content': 'This is the second blog!'
        },
        {
            'author': {'nickname': 'Eric Yuan'},
            'content': 'This is the third blog!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           blogs=blogs)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if  form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)