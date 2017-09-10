from flask import jsonify, g
from flask_restful import Resource

from ..auth import token_required


class UserAPI(Resource):

    @token_required
    def get(self):
        _user = g.current_user

        user = _user.serialize()

        if _user.society:
            user["society"] = _user.society.name
        else:
            user["society"] = None
        logged_activities = [activity.serialize() for activity in
                             _user.activities]
        user["loggedActivities"] = logged_activities
        logged_points = sum([point.value for point in _user.points])
        user["loggedPoints"] = logged_points

        return jsonify(dict(data=user))
