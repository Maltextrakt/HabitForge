# Initializes the application, sets up configurations, registers blueprints, initializes extensions(e.g. SQLAlchemy)

#Imports
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_login import LoginManager

#Initialize extensions
csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()


#Factory method to instantiate the application
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app) # Initialize database with the application
    csrf.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    from app.models import User
    #Function to reload full user object from the session user ID
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from app.auth.routes import auth
    from app.main.routes import main
    from app.dashboard.routes import dashboard

    app.register_blueprint(auth)
    app.register_blueprint(main, url_prefix="/main")
    app.register_blueprint(dashboard, url_prefix="/dashboard")


    return app

