from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager

# creating database
db = SQLAlchemy()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    login_manager.login_view = 'auth.login'
    
    with app.app_context():
        from . import models
        from app import auth, route
        app.register_blueprint(auth.bp)
        app.register_blueprint(route.bp)
    return app
