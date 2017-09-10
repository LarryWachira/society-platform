from api.models import Society, User
from tests.base_test import BaseTestCase


class ModelsTestCase(BaseTestCase):
    """Test models."""

    def test_models(self):
        society = Society(
            color_scheme="#dkneif"
        )

        user = User(
            uuid="-Ktest",
            name="dan",
            email="user@mail.com",
            country="Kenya",
            society=society
        )
        self.assertTrue(user.save())
