"""Contain All App Models."""
import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def generate_uuid():
    return uuid.uuid4()


class Base(db.Model):
    """Base model, contain utility methids and properties."""

    __abstract__ = True
    uuid = db.Column(db.String, primary_key=True, default=generate_uuid)
    name = db.Column(db.String)
    photo = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
            artibute.name: getattr(self, artibute.name)
            for artibute in self.__table__.columns}
        return dictionary_mapping


class User(Base):
    """Models Users."""

    __tablename__ = 'users'
    email = db.Column(db.String)
    role = db.Column(db.String)
    country = db.Column(db.String)
    society_id = db.Column(db.String, db.ForeignKey('societies.uuid'))
    points = db.relationship('Point', backref='user', lazy='dynamic')


class Society(Base):
    """Model Societies in Andela."""

    __tablename__ = 'societies'
    color_scheme = db.Column(db.String)
    logo = db.Column(db.String)
    members = db.relationship('User', backref='society', lazy='dynamic')
    points = db.relationship('Point', backref='society', lazy='dynamic')


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
    approve_date = db.Column(db.DateTime)
    user_id = db.Column(db.String, db.ForeignKey('users.uuid'))
    society_id = db.Column(db.String, db.ForeignKey('societies.uuid'))
    activity_id = db.Column(db.String, db.ForeignKey('activities.uuid'))
