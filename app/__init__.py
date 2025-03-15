# Initializes the application, sets up configurations, registers blueprints, initializes extensions(e.g. SQLAlchemy)

#Imports
from flask import Flask
from app.auth.routes import auth
from app.main.routes import main
from app.dashboard.routes import dashboard
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Factory method to instantiate the application
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app) # Initialize database with the application

    app.register_blueprint(auth)
    app.register_blueprint(main, url_prefix="/main")
    app.register_blueprint(dashboard, url_prefix="/dashboard")


    return app

