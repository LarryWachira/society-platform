"""Contain All App Models."""
import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def generate_uuid():
    """Generate unique string."""
    return str(uuid.uuid1())


def camel_case(snake_str):
    """Convert string to camel case."""
    title_str = snake_str.title().replace("_", "")

    return title_str[0].lower() + title_str[1:]


# many to many relationship between users and activities
user_activity = db.Table('user_activity',
                         db.Column('user_uuid', db.String,
                                   db.ForeignKey('users.uuid'), nullable=False
                                   ),
                         db.Column('activity_uuid', db.String,
                                   db.ForeignKey('activities.uuid'),
                                   nullable=False))


class Base(db.Model):
    """Base model, contain utility methods and properties."""

    __abstract__ = True
    uuid = db.Column(db.String, primary_key=True, default=generate_uuid)
    name = db.Column(db.String)
    photo = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String)

    def __repr__(self):
        """Repl rep of models."""
        return f"{type(self).__name__}(id='{self.uuid}', name='{self.name}')"

    def __str__(self):
        """Return string representation."""
        return self.name

    def save(self):
        """Save the object in DB.

        Returns:
            saved(boolean) true if saved, false otherwise
        """
        saved = None
        try:
            db.session.add(self)
            db.session.commit()
            saved = True
        except Exception:
            saved = False
            db.session.rollback()
        return saved

    def delete(self):
        """Delete the object in DB.

        Returns:
            deleted(boolean) True if deleted else false
        """
        deleted = None
        try:
            db.session.delete(self)
            db.session.commit()
            deleted = True
        except Exception:
            deleted = False
            db.session.rollback()
        return deleted

    def serialize(self):
        """Map model to a dictionary representation.

        Returns:
            A dict object
        """
        dictionary_mapping = {
            camel_case(attribute.name): str(getattr(self, attribute.name))
            for attribute in self.__table__.columns}
        return dictionary_mapping


class User(Base):
    """Models Users."""

    __tablename__ = 'users'
    email = db.Column(db.String)
    role = db.Column(db.String, default="member")
    country = db.Column(db.String)

    society_id = db.Column(db.String, db.ForeignKey('societies.uuid'))

    points = db.relationship('Point', backref='user', lazy='dynamic')
    activities = db.relationship('Activity', secondary='user_activity',
                                 lazy='dynamic', backref='users')


class Society(Base):
    """Model Societies in Andela."""

    __tablename__ = 'societies'
    name = db.Column(db.String, nullable=False, unique=True)
    color_scheme = db.Column(db.String)
    logo = db.Column(db.String)
    _total_points = db.Column(db.Integer, default=0)

    members = db.relationship('User', backref='society', lazy='dynamic')
    points = db.relationship('Point', backref='society', lazy='dynamic')

    @property
    def total_points(self):
        """Keep track of all society points."""
        return self._total_points

    @total_points.setter
    def total_points(self, value):
        self._total_points += value


class Activity(Base):
    """Model activities available for points."""

    __tablename__ = 'activities'
    value = db.Column(db.Integer)
    description = db.Column(db.String, nullable=False)

    points = db.relationship('Point', backref='activity', lazy='dynamic')


class Point(Base):
    """To contain points fields."""

    __tablename__ = 'points'
    value = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, default='pending')
    approved_at = db.Column(db.DateTime)
    approver_id = db.Column(db.String)

    approve_date = db.Column(db.DateTime)

    user_id = db.Column(db.String, db.ForeignKey('users.uuid'))
    society_id = db.Column(db.String, db.ForeignKey('societies.uuid'))
    activity_id = db.Column(db.String, db.ForeignKey('activities.uuid'))

    def __repr__(self):
        return '<Point by {}>'.format(self.user)
