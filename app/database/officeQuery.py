import psycopg2
from app.database.connection import databasem
from app.database.createTable import CreateTables

class OfficeQueries():
    def __init__(self):

        self.connect = databasem().connectdb()
        self.cursors = self.connect.cursor()
        self.users_list = []
    def add_candidate(self,office,party,userId):
        insert_query = "INSERT INTO candidate(office,party,candidate) VALUES (%s,%s,%s) RETURNING office,candidate"
        self.cursors.execute(insert_query,
                             (office,party,userId))
        self.connect.commit()
        rows = self.cursors.fetchone()
        candidatelist = {
            "office": rows[0],
            "candidate": rows[1],
            
        }
        return candidatelist  

    def add_office(self,type,name):
        insert_query="INSERT INTO Office(type,name) VALUES (%s,%s) RETURNING "
