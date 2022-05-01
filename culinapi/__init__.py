from flask import Flask 

from .extensions import db, migrate, cogauth
from .routes.main import main
from .routes.api import api

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["COGNITO_REGION"] = "us-east-1"
    app.config["COGNITO_USERPOOL_ID"] = "us-east-1_WMfyjujOB"

    db.init_app(app)
    migrate.init_app(app, db)
    cogauth.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(api,url_prefix="/api")

    return app