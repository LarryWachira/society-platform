from api.models import Activity, Point, Society, User
from tests.base_test import BaseTestCase


class ModelsTestCase(BaseTestCase):
    """Test models."""

    def test_models(self):
        society = Society(
            color_scheme="#dkneif"
        )

        user = User(
            name="dan",
            email="user@mail.com",
            role="member",
            country="Kenya",
            society=society
        )
        self.assertTrue(user.save())
