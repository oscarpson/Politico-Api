import psycopg2
import os


class databasem():
    def connectdb(self):
        conn = psycopg2.connect(
            user="postgres",
            password="",
            host="localhost",
            port="5432",
            database="politico")
        #cursor = conn.Cursor()
        return conn
