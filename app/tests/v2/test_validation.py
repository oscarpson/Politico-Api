import unittest
from app.tests.v2.base_test import BaseTest


class ApiValidationV2(BaseTest):
    def test_validate_partyjson(self):
        resp = self.client().post(
            '/api/v2/auth/signup',
            data=self.add_user,
            content_type='text/plain')
        self.assertEqual(resp.status_code, 400)
