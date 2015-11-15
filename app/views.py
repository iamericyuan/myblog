__author__ = 'Eric Yuan'

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/comment')
def comment():
    return render_template('comment.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')