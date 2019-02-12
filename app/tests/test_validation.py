import unittest
from app.tests.base_test import BaseTest


class PoliticalValidation(BaseTest):
    def test_validate_partyjson(self):
        resp = self.client1.post(
            '/api/v1/parties', data=self.add_party, content_type='text/plain')
        self.assertEqual(resp.status_code, 400)

    def test_validate_partyid(self):
        self.client().post('/api/v1/parties', data=self.add_party,
                           content_type='application/json')
        resp = self.client().delete('/api/v1/parties/B', data=self.add_party,
                                    content_type='application/json')
        print(resp.json)
        self.assertEqual(resp.json[0]["status"], 400)
