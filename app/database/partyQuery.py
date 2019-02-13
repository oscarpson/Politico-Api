import psycopg2
from app.database.connection import databasem
from app.database.createTable import CreateTables


#self.conct=conn
class PartyQueries():
    def __init__(self):

        self.connect = databasem().connectdb()
        self.cursors = self.connect.cursor()
        self.users_list = []

    def create_party(self, name, hqAddress, logoUrl, createdBy):
        insert_query = "INSERT INTO Party(name,hqAddress,logoUrl,createdby) VALUES (%s,%s,%s,%s) RETURNING id,name,hqAddress,logoUrl"
        self.cursors.execute(insert_query,
                             (name, hqAddress, logoUrl, createdBy))
        self.connect.commit()
        rows = self.cursors.fetchone()
        partyRow = {
            "id": rows[0],
            "name": rows[1],
            "hqAddress": rows[2],
            "logoUrl": rows[3]
        }
        return partyRow

    def get_all_parties(self):
        parties_list = []
        all_parties_query = "SELECT * FROM Party"
        self.cursors.execute(all_parties_query)
        self.connect.commit()
        rows = self.cursors.fetchall()
        for row in rows:
            partyRow = {
                "id": rows[0],
                "name": rows[1],
                "hqAddress": rows[2],
                "logoUrl": rows[3]
            }
            parties_list.append(partyRow)
        return parties_list

    def get_specific_party(self, id):
        get_query = "SELECT * FROM Party WHERE id =%s"
        self.cursors.execute(get_query, (id))
        self.connect.commit()
        rows = self.cursors.fetchone()
        partyRow = {
            "id": rows[0],
            "name": rows[1],
            "hqAddress": rows[2],
            "logoUrl": rows[3]
        }
        return partyRow

    def delete_party(self, id):
        delete_query = "DELETE FROM Party WHERE id=%s"
        self.cursors.execute(delete_query, (id))
        self.connect.commit()

        partyRow = {"status": 200, "data": "deleted successfuly"}
