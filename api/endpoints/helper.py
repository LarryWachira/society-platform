"""Contain utility functions and constants."""


def serialize_point(point):
    """Map point object to dict representation.

    Args:
       point(Point): point object

    Returns:
       serialized_point(dict): dict representation of point
    """
    serialized_point = point.serialize()
    serialized_point["id"] = serialized_point.pop("uuid")
    serialized_point["activity"] = point.activity.name
    serialized_point["owner"] = point.user.name

    return serialized_point
