import json

from api.models import User
from tests.base_test import BaseTestCase


class UserTestCase(BaseTestCase):
    """Test users endpoints."""

    def test_models(self):
        response = self.client.get('api/v1/user/profile', headers=self.header)

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.get_data(as_text=True))
        user_id = response_json['data']['uuid']
        user_name = response_json['data']['name']
        user = User.query.get(user_id)

        self.assertEqual(user_name, user.name)
