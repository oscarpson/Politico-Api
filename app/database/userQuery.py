import psycopg2
from app.database.connection import databasem
from app.database.createTable import CreateTables


#self.conct=conn
class UserQueries():
    def __init__(self):

        self.connect = databasem().connectdb()
        self.cursors = self.connect.cursor()
        self.users_list = []

    def create_user(self, firstname, lastname, othername, email, phoneNumber,
                    passportUrl, isAdmin):
        insert_query = "INSERT INTO Puser(firstname,lastname,othername,email,phoneNumber,passportUrl,isAdmin) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id, firstname,lastname,othername,email,phoneNumber,passportUrl,isAdmin"
        self.cursors.execute(insert_query,
                             (firstname, lastname, othername, email,
                              phoneNumber, passportUrl, isAdmin))
        self.connect.commit()
        rows = self.cursors.fetchone()
        userslist = {
            "firstname": rows[0],
            "lastname": rows[1],
            "othername": rows[2],
            "email": rows[3],
            "phoneNumber": rows[4],
            "passportUrl": rows[5],
            "isAdmin": rows[6]
        }
        return userslist
