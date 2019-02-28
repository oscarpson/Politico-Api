import psycopg2
from app.database.connection import databasem
from app.database.createTable import CreateTables


class OfficeQueries():
    def __init__(self):

        self.connect = databasem().connectdb()
        self.cursors = self.connect.cursor()
        self.users_list = []

    def add_candidate(self, office, party, userId):
        insert_query = "INSERT INTO candidate(office,party,candidate) VALUES (%s,%s,%s) RETURNING office,candidate"
        self.cursors.execute(insert_query, (office, party, userId))
        self.connect.commit()
        rows = self.cursors.fetchone()
        candidatelist = {
            "office": rows[0],
            "candidate": rows[1],
        }
        return candidatelist

    def add_office(self, type, name):
        insert_office_query = "INSERT INTO Office(type,name) VALUES (%s,%s) RETURNING type,name"
        self.cursors.execute(insert_office_query, (type, name))
        self.connect.commit()
        office_row = self.cursors.fetchone()
        office_list = {"type": office_row[0], "name": office_row[1]}
        return office_list

    def voting_results(self, officeId):
        vote_list = "SELECT VOTE.OFFICE,VOTE.CANDIDATE,COUNT(*) FROM VOTE  WHERE vote.office = %s GROUP BY office,candidate;"
        self.cursors.execute(vote_list, officeId)
        self.connect.commit()
        vlist = []
        votes = self.cursors.fetchall()
        for vote_row in votes:
            votelist = {
                "office": vote_row[0],
                "candidate": vote_row[1],
                "results": vote_row[2]
            }
            vlist.append(votelist)
        return vlist
