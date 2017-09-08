"""Module to house setup, teardown and utility class for testing."""

from unittest import TestCase

from api.models import db
from app import create_app


class BaseTestCase(TestCase):
    """Contain utility required for testing."""

    def setUp(self):
        """Setup function to configure test enviroment."""

        self.app = create_app('Testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

        # test client
        self.client = self.app.test_client()

    def tearDown(self):
        """Clean up after every test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
