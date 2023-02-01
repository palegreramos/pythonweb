from flask import Flask, render_template,request,url_for
from app import *

@app.route('/')
def inicial():
    return render_template('index.html')

@app.route('/home')
def home():
    return "Hello Flask!"

