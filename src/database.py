from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_db(app):
    """Initializes nonexistent database tables."""

    with app.app_context():
        db.create_all()
    print("created db tables:", db.metadata.tables.keys())

