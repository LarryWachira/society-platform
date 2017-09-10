"""Module to house setup, teardown and utility class for testing."""

from unittest import TestCase
import datetime

from jose import jwt

from api.models import db
from app import create_app


class BaseTestCase(TestCase):
    """Contain utility required for testing."""
    exp_date = datetime.datetime.utcnow()
    test_payload = {
        "UserInfo": {
            "email": "test.test@andela.com",
            "first_name": "test",
            "id": "-Ktest_id",
            "last_name": "test",
            "name": "test test",
            "picture": "https://www.link.com",
            "roles": {
                    "Andelan": "-Ktest_andelan_id",
                    "Fellow": "-Ktest_fellow_id"
            }
        },
        "exp": exp_date + datetime.timedelta(days=1)
    }

    def setUp(self):
        """Setup function to configure test enviroment."""

        self.app = create_app("Testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

        # test client
        self.client = self.app.test_client()

        # header
        self.header = {
            "Authorization": self.generate_token(self.test_payload)
        }

    @staticmethod
    def generate_token(payload):
        """ Generates token """

        token = jwt.encode(payload, "secret", algorithm="HS256")
        return token

    def tearDown(self):
        """Clean up after every test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
