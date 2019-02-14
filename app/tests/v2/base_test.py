import unittest
import pytest
import json
from app.api.v2 import views
from app.api.app import create_app


class BaseTest(unittest.TestCase):
    def setUp(self):

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.client1 = self.app.test_client()

        self.add_office = json.dumps({"type": "Government", "name": "Senate"})
        self.add_party = json.dumps({
            "name": "Chaa chetu",
            "hqAddress": "Thika",
            "logoUrl": "images"
        })
        self.add_user = json.dumps({
            "firstname": "oscar",
            "lastname": "muigai",
            "othername": "baba yao",
            "email": "gmail",
            "phoneNumber": "0708369044",
            "passportUrl": "images/url",
            "isAdmin": True
        })
        self.add_vote = json.dumps({
            "createdOn": "22/11/2017",
            "userId": 2,
            "officeId": 5,
            "candidateId": 1
        })

        self.add_candidate = json.dumps({"office": 4, "party": 2, "userId": 2})

    def tearDown(self):
        self.app.testing = False
