# Initializes the application, sets up configurations, registers blueprints, initializes extensions(e.g. SQLAlchemy)

#Imports
from flask import Flask
from app.routes import main


#Factory method to instantiate the application
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(main)


    return app

