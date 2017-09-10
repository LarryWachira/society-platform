"""Models TestSuite."""

from api.models import Activity, Point, Society, User
from tests.base_test import BaseTestCase


class UserTestCase(BaseTestCase):
    """Test models."""

    def test_models(self):
        society = Society(
            name="Phoenix",
            color_scheme="#333333",
            logo="https://logo.png",
            photo="http://photo.url2"
        )

        user = User(
            uuid="-Ktest",
            name="dan",
            email="user@mail.com",
            country="Kenya",
            society=society
        )
        self.assertTrue(user.save())

    def test_user_instance(self):
        """Test user properties/relationships."""
        new_user = User(email="someonecool.andela.com",
                        name="thecoolest",
                        uuid="-Ksomeid",
                        role="member",
                        country="ke/ug/niger/ny/sa/tz/rw")
        self.assertTrue(new_user.save())

        query_user = User.query.filter_by(uuid="-Ksomeid").first()
        self.assertTrue(query_user == new_user)


class SocietyTestCase(BaseTestCase):
    """Test Society model."""

    def test_society_instance(self):
        """Test society properties/relationships."""
        new_society = Society(name="istelle",
                              photo="url/imgae",
                              logo="url/image",
                              color_scheme="#00ff4567")
        self.assertTrue(new_society.save())

        query_society = Society.query.filter_by(name="istelle").first()
        self.assertTrue(query_society == new_society)


class PointTestCase(BaseTestCase):
    """Test Point model."""

    def test_points_instance(self):
        """Test point properties/relationships."""
        point = Point(value=2500,
                      name="interview-2017-sep-23rd")

        self.assertTrue(point.save())

        query_point = Point.query.filter_by(
            name="interview-2017-sep-23rd").first()
        self.assertTrue(query_point == point)


class ActivityTestCase(BaseTestCase):
    """Test Activity model."""

    def test_activity_instance(self):
        """Test activity properties/relationships."""
        activity = Activity(name="Interview",
                            value=50,
                            description="members eran 50 points per activity",
                            photo="cool/icon/url")

        self.assertTrue(activity.save())

        querty_activity = Activity.query.filter_by(name="Interview").first()

        self.assertTrue(activity == querty_activity)
