from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db
from app.user import users_blueprint
from app.menu import menu_blueprint

def create_app() :
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)

    with app.app_context() :
        db.create_all()
        db.session.commit()

    app.register_blueprint(users_blueprint, url_prefix='/users')
    app.register_blueprint(menu_blueprint, url_prefix='/menu')

    return app
