import psycopg2
from app.database.connection import databasem
import psycopg2.extras as extra


#self.conct=conn
class UserModelClass():
    def __init__(self):

        self.connect = databasem().connectdb()
        self.cursors = self.connect.cursor()
        self.users_list = []
        #cursors.execute("INSERT INTO users(username,email) VALUES ('kiki','mail')")
        #databasem().connectdb().commit()
    def create_user(self, name, email):
        insert_query="INSERT INTO users(username,email) VALUES (%s,%s) RETURNING id, username,email"
        self.cursors.execute(insert_query,(name,email))
        
        rows = self.cursors.fetchone()
        userslist = {"id": rows[0], "name": rows[1], "email": rows[2]}
        return userslist
