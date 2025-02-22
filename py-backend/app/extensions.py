from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta

from config import Config

db = SQLAlchemy()
#  Object Relational Mapper
orm = db.orm

# DB Engine
Engine = db.create_engine(
  Config.SQLALCHEMY_DATABASE_URI,
  pool_size=20,
  max_overflow=5
)

# JWT Manager
jwt = JWTManager()

# CORS
cors = CORS()

# function to translate a data map from a db transaction to serialiabe JSON
def to_dict(data_map):
  new_dict = []
  for row in data_map:
    row_dict = {}
    for key in row.keys():
      row_dict[key] = row[key]   
    
    new_dict.append(row_dict)

  return new_dict