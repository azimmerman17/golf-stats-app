from datetime import datetime

from app.extensions import db, orm
from app.models.user import USER

# Model Contains Security Information for Users - None of this table data should every be visable on frontend!!!
class USER_AUTH(db.Model):
  AUTH_ID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  USER_ID = db.Column(db.Integer, db.ForeignKey(USER.USER_ID, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  SALT = db.Column(db.String(50), nullable=False)
  PASSWORD_HASH = db.Column(db.String(100), nullable=False)
  GUID_TOKEN = db.Column(db.String(50), nullable=False)
  GUID_EXPIRE = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())
  CREATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())
  UPDATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())
