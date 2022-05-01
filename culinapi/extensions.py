from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_cognito import CognitoAuth

db = SQLAlchemy()
migrate = Migrate()


cogauth = CognitoAuth()