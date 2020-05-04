from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.models import db
from app.user import users_blueprint
from app.menu import menu_blueprint
from app.student import student_blueprint
from app.order import order_blueprint

def create_app() :
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    CORS(app)
    db.init_app(app)

    with app.app_context() :
        db.create_all()
        db.session.commit()

    app.register_blueprint(users_blueprint, url_prefix='/user')
    app.register_blueprint(menu_blueprint, url_prefix='/menu')
    app.register_blueprint(student_blueprint, url_prefix='/student')
    app.register_blueprint(order_blueprint, url_prefix='/order')

    return app
