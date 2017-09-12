"""Contain utility functions and constants."""


def serialize_point(point):
    """Map point object to dict representation.

    Args:
       point(Point): point object

    Returns:
       serialized_point(dict): dict representation of point
    """
    serialized_point = point.serialize()
    serialized_point["pointName"] = serialized_point.pop("name")
    serialized_point["name"] = point.activity.name
    serialized_point["owner"] = point.user.name
    serialized_point["pointDescription"] = serialized_point.pop("description")
    serialized_point["description"] = point.activity.description

    return serialized_point
