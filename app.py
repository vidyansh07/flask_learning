from flask import Flask

app = Flask(__name__)

@app.route('/')
# this app.route is called decorator
# it is used to bind a function to a URL

def welcome():
    return "Welcome here"


@app.route('/home')
# this app.route is called decorator
# it is used to bind a function to a URL

def home():
    return "Welcome to home"

from controller import *