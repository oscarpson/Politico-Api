import psycopg2
from app.database.connection import databasem
import psycopg2.extras as extra


class CreateTables():
    def __init__(self):
        self.conn = databasem().connectdb()
        self.cursors = self.conn.cursor()

    def tables(self):
        tab_list = self.create_tables()
        for table in tab_list:
            self.cursors.execute(table)
            self.conn.commit()

    def create_tables(self):

        create_user_query = """CREATE TABLE IF NOT EXISTS Puser(id serial PRIMARY KEY,
                firstname Varchar(50) NOT NULL,lastname Varchar(50) NOT NULL,
                othername Varchar(50) NOT NULL,email Varchar(50) NOT NULL,
                phoneNumber Varchar(20) NOT NULL,passportUrl Varchar(100) NOT NULL,
                isAdmin BOOLEAN NOT NULL )"""

        create_user_query = """CREATE TABLE IF NOT EXISTS Office (id serial PRIMARY KEY,type Varchar(50) NOT NULL,name Varchar(50))"""

        create_party_query = """CREATE TABLE IF NOT EXISTS Party(id serial PRIMARY KEY,
                name Varchar(50) NOT NULL,hqAddress Varchar(50) NOT NULL,
                logoUrl Varchar(50) NOT NULL,createdBy Varchar(50) NOT NULL)"""

       
            

        table_list = [create_user_query, create_user_query, create_party_query]
        return table_list
