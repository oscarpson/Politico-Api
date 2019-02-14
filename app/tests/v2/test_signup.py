import unittest
from app.tests.v2.base_test import BaseTest


class UserSignup(BaseTest):
    def test_user_signup(self):
        resp = self.client().post(
            '/api/v2/auth/signup',
            data=self.add_user,
            content_type='application/json')

        self.assertEqual(resp.status_code, 201)


if __name__ == '__main__':
    unittest.main()
