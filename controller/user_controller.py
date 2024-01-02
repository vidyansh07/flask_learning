from app import app
from model.user_model import user_model

# This is the controller for user signup
# It calls the user_signup_model() from user_model.py
# and returns the result to the client


@app.route('/user/getall')
# this app.route is called decorator
# it is used to bind a function to a URL

def user_getall_controller():
    return user_model().user_getall_controller()

