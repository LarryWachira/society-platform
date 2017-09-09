from flask import jsonify
from flask_restplus import Resource

from ..auth import token_required
from ..models import Activity


class ActivitiesAPI(Resource):

    @token_required
    def get(self):
        activities = Activity.query.all()

        activities_list = []

        for _activity in activities:
            activity = _activity.serialize()
            activity_points = _activity.points
            activity['totalPointsLogged'] = sum([point.value for point in
                                                 activity_points])
            activities_list.append(activity)

        return jsonify(dict(data=activities_list))
