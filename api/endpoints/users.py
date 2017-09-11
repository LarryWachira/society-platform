"""Module for Users in platform."""
from flask import g, jsonify
from flask_restplus import Resource

from ..auth import token_required


class UserAPI(Resource):
    """User Resource."""

    @token_required
    def get(self):
        """Get user information."""
        _user = g.current_user
        user = _user.serialize()

        if _user.society:
            user["society"] = _user.society.name
        else:
            user["society"] = None

        logged_activities = []
        user_points = _user.points
        for _point in user_points:
            _activity = _point.activity
            activity = _activity.serialize()
            activity['status'] = _point.status
            activity['createdAt'] = _point.created_at
            activity['pointName'] = _point.name
            activity['pointDescription'] = _point.description
            activity['value'] = _point.value
            activity['timesLogged'] = len(user_points.filter_by(
                activity_id=_activity.uuid).all())
            logged_activities.append(activity)

        user["loggedActivities"] = logged_activities
        logged_points = sum([point.value for point in _user.points])
        user["totaLoggedPoints"] = logged_points

        return jsonify(dict(data=user))
