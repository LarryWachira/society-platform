import json

from api.models import Activity
from tests.base_test import BaseTestCase


class ActivitiesTestCase(BaseTestCase):
    """Test activities endpoints."""

    def test_models(self):
        response = self.client.get('api/v1/activities', headers=self.header)

        self.assertEqual(response.status_code, 200)

        activities = Activity.query.all()
        response_json = json.loads(response.get_data(as_text=True))

        self.assertEqual(len(activities), len(response_json['data']))
