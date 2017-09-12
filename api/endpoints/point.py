"""Module for Points Resources."""
from api.auth import roles_required, token_required
from api.models import Activity, Point, Society, User
from flask import g
from flask_restplus import Resource, reqparse

from .helper import serialize_point


class PointResource(Resource):
    """Point Resource."""

    def __init__(self, r):
        """Initialize resource."""
        self.ALL_SOCIETIES = Society.query.all()
        self.parser = reqparse.RequestParser()

    def get(self):
        """Get all the points filtered by the query param."""
        # get client query params
        self.parser.add_argument('user_id', location='args')
        self.parser.add_argument('activity_id', location='args')
        self.parser.add_argument('society_id', location='args')
        args = self.parser.parse_args()

        activity_id = args.get('activity_id')
        user_id = args.get('user_id')
        society_id = args.get('society_id')

        # Validation
        if user_id and not User.query.filter_by(uuid=user_id).first():
            return {"error": "Invalid User id"}, 400

        elif activity_id and not Activity.query.filter_by(
                uuid=activity_id).first():
            return {"error": "Invalid activity id"}, 400

        elif society_id and not Society.query.filter_by(
                uuid=society_id).first():
            return {"error": "Invalid society_id"}, 400

        response = {}
        if user_id and activity_id:
            values = Point.query.order_by(Point.created_at).filter_by(
                user_id=user_id)
            response["points"] = list(map(
                serialize_point,
                values.filter_by(activity_id=activity_id).all()))

        elif society_id and activity_id:
            values = Point.query.order_by(Point.created_at).filter_by(
                society_id=society_id)
            response["points"] = list(map(
                serialize_point,
                values.filter_by(activity_id=activity_id).all()))

        elif user_id:
            values = Point.query.order_by(Point.created_at).filter_by(
                user_id=user_id)
            response["points"] = list(map(serialize_point, values.all()))

        elif activity_id:
            values = Point.query.order_by(Point.created_at).filter_by(
                activity_id=activity_id)
            response["points"] = list(map(serialize_point, values))

        elif society_id:
            values = Point.query.order_by(Point.created_at).filter_by(
                society_id=society_id).all()
            response["points"] = list(map(serialize_point, values))

        else:
            response = {
                society.name: {
                    "total_points": society.total_points,
                    "society_id": society.uuid,
                    "description": society.description}
                for society in self.ALL_SOCIETIES}

            return response, 200

        pending_point = list(filter(
            lambda point: point["status"] == "pending", response["points"]))
        approved_point = list(filter(
            lambda point: point["status"] == "APPROVED", response["points"]))
        rejected_point = list(filter(
            lambda point: point["status"] == "REJECTED", response["points"]))
        inprogress_point = list(filter(
            lambda point: point["status"] == "INPROGRESS", response["points"]))

        total = sum([int(point["value"]) for point in approved_point])
        total_p = sum([int(point["value"]) for point in pending_point])
        total_r = sum([int(point["value"]) for point in rejected_point])
        total_inp = sum([int(point["value"]) for point in inprogress_point])

        response["totalPendingPoints"] = total_p
        response["totalRejectedPoints"] = total_r
        response["totalInprogressPoints"] = total_inp
        response["totalPointsAproved"] = total

        response["points"].reverse()
        return response, 200

    @token_required
    def post(self):
        """Post points earned for an activity."""
        self.parser.add_argument('activity_id', required=True)
        self.parser.add_argument('value', required=True, type=int)
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('description')
        args = self.parser.parse_args()

        user = g.current_user

        activity = Activity.query.filter_by(
            uuid=args.get('activity_id')).first()
        if not activity:
            return {"error": "Invalid actvity Id"}, 400

        if not args.get('value'):
            return {"error": "Value can not be less than 1."}, 400

        if args.get('value') < 1:
            return {"error": "Quantity must be greater than 1."}, 400

        name = args.get('name')
        if user.points.filter_by(name=name).first():
            return {"error":
                    f"You have already logged: {name}, please edit it."}, 400

        point = Point(
            value=activity.value * args.get('value'),
            name=args.get('name'),
            description=args.get('description') or "Not Available.")

        user.points.append(point)
        activity.points.append(point)
        user.society.points.append(point)

        if point.save():
            return serialize_point(point), 201
        return {"error": f"Server unable to create point:{point.name}."}, 500

    @token_required
    def put(self):
        """Modify points submitted."""
        self.parser.add_argument('point_id', required=True)
        self.parser.add_argument('name')
        self.parser.add_argument('value', type=int)
        self.parser.add_argument('description')
        args = self.parser.parse_args()

        point = Point.query.filter_by(uuid=args.get('point_id')).first()
        if not point:
            return {"error": "Invalid point_id"}, 400

        value = args.get('value')
        if (value or value == 0) and value < 1:
            return {"error": "Value can not be less than 1."}, 400

        elif value == point.value:
            return {"error": "Values are the same, can not update."}, 409

        elif not value and not args.get('description'):
            return {"error": "Provide value or description to update."}, 422

        elif not (point.user_id == g.current_user.uuid):
            return{"error": "Permission denied: user not allowed"}, 403

        if value:
            point.value = value

        if args.get('name'):
            point.name = args.get('name')

        if args.get('description'):
            point.description = args.get('description')

        if point.save():
            return serialize_point(point), 200
        return {"error": f"Server unable to update point: {point.name}."}, 500

    @token_required
    def patch(self):
        """Patch points submitted."""
        self.parser.add_argument('point_id', required=True)
        self.parser.add_argument('status', required=True)
        args = self.parser.parse_args()

        status = args.get('status')

        STATUS = ("APPROVED", "REJECTED", "INPROGRESS")
        if not status or status.upper() not in STATUS:
            return{"error":
                   f"Status should be one of: {', '.join(STATUS)}"}, 400

        point = Point.query.filter_by(uuid=args.get('point_id')).first()
        if not point:
            return {"error": "Invalid point id"}, 400

        if not (point.status == STATUS[0]) and status.upper() == STATUS[0]:
            point.society.total_points = point.value

        if point.status == STATUS[0] and status.upper() == STATUS[1]:
            point.society.total_points = -point.value

        point.status = status.upper()

        if point.save():
            return serialize_point(point), 200
        return {"error": f"Server unable to update point: {point.name}."}, 500

    @token_required
    def delete(self):
        """Delete a given point."""
        self.parser.add_argument('point_id', required=True)
        args = self.parser.parse_args()

        point = Point.query.filter_by(uuid=args.get('point_id')).first()

        if not point:
            return {"error": "Inavlid point id"}, 400

        elif not (point.user_id == g.current_user.uuid):
            return{"error":
                   "Permission denied: user not allowed"}, 403

        if point.delete():
            return {"data": "deleted succesful."}, 200
        return {"error": f"Server unable to delete point: {point.name}."}, 500
