from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.extensions import db
from config import Config

# FACILITY MODELS
from app.models import facility, course, tee, rating, hole

def create_app(config_class=Config):
  app = Flask(__name__)

  # Set Config varibles
  app.config.from_object(config_class)

  # Initialize Flask extensions
  db.init_app(app)

  # Migrate Models  
  Migrate(app,facility.db)
  Migrate(app,course.db)
  Migrate(app,tee.db)
  Migrate(app,rating.db)
  Migrate(app,hole.db)

  # Register Blueprints
  from app.facility import bp as facility_bp
  app.register_blueprint(facility_bp)

  @app.route('/')
  def hello_world():
      return "<p>Hello, World!</p>"

  return app