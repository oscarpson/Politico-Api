import unittest
import pytest
import json
from app.api.v1 import views
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

    def tearDown(self):
        self.app.testing = False
