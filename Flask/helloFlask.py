#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from markupsafe import escape
from flask import Flask, url_for, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = b'abcdefghijlmnopq'

with app.test_request_context():
	url_for('static', filename = 'test1.html')

# ---------------------------------------------------------------------------

@app.route('/')
def hello_world():

	return redirect(url_for('index_page'))

# ---------------------------------------------------------------------------

@app.route('/index/')
def index_page():

	if 'username' in session:
		userId = escape(session['username'])
	else:
		userId = "NOT LOGGED"

	return render_template('index.html', name = userId)

# ---------------------------------------------------------------------------

# URL http://127.0.0.1:5000/andre/13
@app.route('/<string:username>/<int:num>') # without trailing '/'
def hello_usernum(username, num):

	return f'Hello, {escape(username)}! Your number: {num}'

# ---------------------------------------------------------------------------

# URL http://127.0.0.1:5000/andre/
# URL http://127.0.0.1:5000/andre
@app.route('/<string:username>/')
def hello_user(username):

	return f'Hello, {escape(username)}!'

# ---------------------------------------------------------------------------

# URL http://127.0.0.1:5000/bye/
# URL http://127.0.0.1:5000/bye
@app.route('/bye/') # with trailing '/'
def bye_world():

	return 'Bye, World!'

# ---------------------------------------------------------------------------

# URL methods
@app.route('/method/', methods=['GET', 'POST'])
def getmethod():

	if request.method == 'POST':

		methodPostParam1 = request.form['param1']

		session['param1'] = escape(methodPostParam1) if methodPostParam1 != "" else "not defined"

		return f"method POST: {session['param1']}"

	else:
		if 'param1' in session:
			paramValue = escape(session['param1'])
		else:
			paramValue = 'not defined'
			
		return f"method GET. Param1 = {paramValue}"

# ---------------------------------------------------------------------------

@app.route('/testusr/')
@app.route('/testusr/<name>/')
def hello(name = None):

	return render_template('temp.html', name = name)

# ---------------------------------------------------------------------------

@app.route('/login/', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index_page'))

	return '''
	       <form method="post">
	       <p><input type=text name=username>
	       <p><input type=submit value=Login>
	       </form>
	       '''

# ---------------------------------------------------------------------------

@app.route('/logout/')
def logout():

	session.pop('username', None)
	return redirect(url_for('index_page'))

# ---------------------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(error):

	return render_template('page_not_found.html'), 404
