import mysql.connector
import json

class user_model:
    
    def __init__(self):
        # Connector establish code
        try :
            self.con = mysql.connector.connect(host="localhost",user= "root", password ="agtma",database ="flask_tutorial")
            self.cur = self.con.cursor(dictionary = True)
            
            print("connection successful")
        except:
            print("Error in connection")
        # Query execution code
        pass
    
    def user_getall_controller(self):
        # Connector establish code
        # Query execution code
        self.cur.execute("SELECT * FROM users")

        # Fetching the result
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "no data found"