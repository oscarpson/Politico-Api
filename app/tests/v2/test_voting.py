import unittest
from app.tests.v2.base_test import BaseTest


class UserVote(BaseTest):
    def test_user_voting(self):
        resp = self.client().post(
            '/api/v2/vote',
            data=self.add_vote,
            content_type='application/json')

        self.assertEqual(resp.status_code, 201)


if __name__ == '__main__':
    unittest.main()
