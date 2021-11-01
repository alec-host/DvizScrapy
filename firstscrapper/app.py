#!/usr/bin/python3
'''
author: alex_irungu
technical interview: Dviz: edmunds.
'''
import os
import threading

from queue import Queue
from threading import Thread

from flask import Flask, render_template
from waitress import serve
from flask_bootstrap import Bootstrap 

from form.CustomNameForm import NameForm

from selenium_worker import SeleniumWorker

app = Flask(__name__)

bootstrap = Bootstrap(app) 

app.config['SECRET_KEY'] = 'Dviz:emdmundsquerypage'

@app.route("/index",methods=['GET', 'POST'])
def index():

	form = NameForm()
	selenium_worker = SeleniumWorker()
	que = Queue()
	
	zip = form.zip.data
	radius = form.radius.data
	
	if(form.validate_on_submit):
		if(zip is not None):
			t = Thread(target=lambda q, arg1: q.put(selenium_worker.worker_manager(arg1)), args=(que,[zip,radius]))
			t.start()
			t.join()
			result = que.get()
			
	return render_template("index.html",form=form,name=zip)

@app.route("/hello")
def hello():
	return '<h1>hello from our simple server</h1>'
	
if(__name__ == '__main__'):
	PORT = 5001
	try:
		print('Server started on port ' + str(PORT))
		serve(app, host='0.0.0.0', port=PORT)
	except KeyboardInterrupt:
		exit()