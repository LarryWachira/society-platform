import json

from .base_test import BaseTestCase

from api.models import Society


class SocietyBaseTestCase(BaseTestCase):
    def setUp(self):
        BaseTestCase.setUp(self)
        self.society = Society(
            name="Phoenix",
            color_scheme="#333333",
            logo="https://logo.png",
            photo="http://photo.url2"
        )
        self.society2 = dict(
            name="Invictus",
            colorScheme="#333334",
            logo="https://logo2.png",
            photo="http://photo.url"
        )
        self.society.save()
    
    def test_society_saved_successfully(self):
        old_societies = Society.query.all()
        post_response = self.client.post(
            '/api/v1/societies/',
            data=json.dumps(self.society2),
            content_type='application/json'
        )
        new_societies = Society.query.all()
        self.assertEqual(
            len(new_societies), len(old_societies) + 1
        )
