from connection import *
import json

def update(name, city, work, username):
    if len(work) == 0:
        conn.cursor().execute("UPDATE user SET name = %s, city = %s WHERE username = %s",(name, city, username))
        conn.commit()
    else:
        
        conn.cursor().execute("UPDATE user SET name = %s, work = %s, city = %s WHERE username = %s", (name, json.dumps(work), city, username))
        conn.commit()
class Person:
    def __init__(self, name, city="Roorkee", work = []):
        self.name = name
        self.city = city
        if len(work) != 0:
            self.work = work

    def show(self):
        show_this = "My name is {} and my current city is {}".format(self.name, self.city)
        print(show_this)
        return show_this

    def add(self, username):
        update(self.name, self.city, self.work, username)
