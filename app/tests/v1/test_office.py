import unittest
from .base_test import BaseTest


class PoliticalOffice(BaseTest):
    def test_get_an_offices(self):
        resp = self.client().get(
            '/api/v2/offices', content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    # def test_post_an_office(self):
    #     resp = self.client().post(
    #         '/api/v2/offices',
    #         data=self.add_office,
    #         content_type='application/json')
    #     self.assertEqual(resp.status_code, 201)


if __name__ == '__main__':
    unittest.main()
