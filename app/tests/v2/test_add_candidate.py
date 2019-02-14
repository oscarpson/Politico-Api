import unittest
from app.tests.v2.base_test import BaseTest


class AddCandidate(BaseTest):
    def test_add_candidate(self):
        resp = self.client().post(
            '/api/v1/offices/5/register',
            data=self.add_candidate,
            content_type='application/json')

        self.assertEqual(resp.status_code, 201)


if __name__ == '__main__':
    unittest.main()
