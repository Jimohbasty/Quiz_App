from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# creating database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    with app.app_context():
        from . import models
        from app import auth
        app.register_blueprint(auth.bp)
    return app
