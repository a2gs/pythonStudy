#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from markupsafe import escape
from flask import request
from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
	return redirect(url_for('index_page'))

@app.route('/index/')
def index_page():
	return render_template('index.html')

# http://127.0.0.1:5000/andre/13
@app.route('/<string:username>/<int:num>') # without trailing '/'
def hello_usernum(username, num):
	return f'Hello, {escape(username)}! Your number: {num}'

# http://127.0.0.1:5000/andre/
# http://127.0.0.1:5000/andre
@app.route('/<string:username>/')
def hello_user(username):
	return f'Hello, {escape(username)}!'

# http://127.0.0.1:5000/bye/
# http://127.0.0.1:5000/bye
@app.route('/bye/') # with trailing '/'
def bye_world():
	return 'Bye, World!'

@app.route('/method/', methods=['GET', 'POST'])
def getmethod():
	if request.method == 'POST':
		return f"method POST: {request.form['param1']}"
	else:
		return 'method GET'

@app.route('/testusr/')
@app.route('/testusr/<name>/')
def hello(name = None):
	return render_template('temp.html', name = name)

with app.test_request_context():
	url_for('static', filename = 'test1.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
