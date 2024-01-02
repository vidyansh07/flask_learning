import mysql.connector

class user_model:
    
    def __init__(self):
        # Connector establish code
        try :
            con = mysql.connector.connect(host="localhost",user= "root", password ="agtma",database ="flask_tutorial")
            print("connection successful")
        except:
            print("Error in connection")
        # Query execution code
        pass
    
    def user_signup_model(self):
        # Connector establish code
        # Query execution code
        return "This is signup operation"