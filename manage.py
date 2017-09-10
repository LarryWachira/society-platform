"""Entry point for app, contain commands to configure and run the app."""

import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, prompt_bool

from api.models import db
from api.initial_data import all_data
from app import create_app

app = create_app(environment=os.environ.get('APP_SETTINGS', "Development"))
manager = Manager(app)
Migrate(app=app, db=db)


@manager.command
def drop_database():
    """Drop database tables."""
    if prompt_bool("Are you sure you want to lose all your data"):
        try:
            db.drop_all()
            print("Dropped all tables susscefully.")
        except Exception:
            print("Failed, make sure your database server is running!")


@manager.command
def create_database():
    """Create database tables from sqlalchemy models."""
    try:
        db.create_all()
        print("Created tables successfully.")
    except Exception:
        db.session.rollback()
        print("Failed, make sure your database server is running!")


@manager.command
def seed():
    """Seed database tables with initial data"""
    if prompt_bool("\n\n\nThis operation will remove all existing data."
                   " Are you sure you want to continue?"):
        try:
            db.drop_all()
            db.create_all()
            db.session.add_all(all_data)
            print("\n\n\nTables seeded successfully.\n\n\n")
        except Exception:
            db.session.rollback()
            print("\n\n\nFailed, make sure your database server is running!\n\n\n")


def shell():
    """Make a shell/REPL context available."""
    return dict(app=create_app(),
                db=db)


manager.add_command("shell", Shell(make_context=shell))
manager.add_command("database", MigrateCommand)


if __name__ == "__main__":
    manager.run()
