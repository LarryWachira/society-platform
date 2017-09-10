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

        logged_activities = []
        for _activity in _user.activities:
            activity = _activity.serialize()
            activity['status'] = _activity.points.filter_by(
                activity_id=_activity.uuid, user_id=_user.uuid).first().status
            logged_activities.append(activity)
            activity['timesLogged'] = len(_user.activities.filter_by(
                name=_activity.name).all())

        user["loggedActivities"] = logged_activities
        logged_points = sum([point.value for point in _user.points])
        user["loggedPoints"] = logged_points

        return jsonify(dict(data=user))
