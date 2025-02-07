from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app.extensions import db, jwt, cors
from config import Config

# FACILITY MODELS
from app.models import facility, course, tee, rating, hole
# USER MODELS
from app.models import user, user_auth


def create_app(config_class=Config):
  app = Flask(__name__)

  # Set Config varibles
  app.config.from_object(config_class)

  # Initialize Flask extensions
  db.init_app(app)
  jwt = JWTManager(app)
  cors = CORS(app, resources={r'/*': {'origins': 'http://localhost:5173'}})   

  # Migrate Models  
  Migrate(app,facility.db)
  Migrate(app,course.db)
  Migrate(app,tee.db)
  Migrate(app,rating.db)
  Migrate(app,hole.db)
  Migrate(app,user.db)
  Migrate(app,user_auth.db)


  # Register Blueprints
  from app.facility import bp as facility_bp
  app.register_blueprint(facility_bp)

  from app.user import bp as user_bp
  app.register_blueprint(user_bp)

  from app.auth import bp as auth_bp
  app.register_blueprint(auth_bp)

  @app.route('/')
  def hello_world():
      return '<p>Hello, World!</p>'

  @app.route('/*')
  def hello_error():
      return '<p>Hello, Error!</p>'

  return app