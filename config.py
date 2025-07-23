# Configuration for the app, secret key

#imports
from flask import Flask
import os


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret")
    DEBUG = True
