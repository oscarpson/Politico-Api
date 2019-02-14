import psycopg2
from app.database.connection import databasem
from app.database.createTable import CreateTables


class VoteQueries():
    def __init__(self):

        self.connect = databasem().connectdb()
        self.cursors = self.connect.cursor()

    def vote(self, createdOn, userId, officeId, candidateId):
        insert_query = "INSERT INTO vote(createdOn,createdBy,office,candidate) VALUES (%s,%s,%s,%s) RETURNING createdBy, office,candidate"
        self.cursors.execute(insert_query,
                             (createdOn, userId, officeId, candidateId))
        self.connect.commit()
        rows = self.cursors.fetchone()
        voteslist = {"voter": rows[0], "office": rows[1], "candidate": rows[2]}
        return voteslist
