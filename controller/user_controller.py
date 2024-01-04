from app import app
from model.user_model import user_model
from flask import request

# This is the controller for user signup
# It calls the user_signup_model() from user_model.py
# and returns the result to the client

@app.route('/user/getall')
# this app.route is called decorator
# it is used to bind a function to a URL

def user_getall_controller():
    return user_model().user_getall_controller()

@app.route("/user/addone", methods = ["POST"])

def user_addone_controller():
    
    return user_model().user_addone_controller(request.form)

