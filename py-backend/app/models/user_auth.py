from datetime import datetime

from app.extensions import db, orm
from app.models.user import USERS

# Model Contains Security Information for Users - None of this table data should every be visable on frontend!!!
class USER_AUTH(db.Model):
  AUTH_ID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  USER_ID = db.Column(db.Integer, db.ForeignKey(USERS.USER_ID, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  SALT = db.Column(db.String(50), nullable=False)
  PASSWORD_HASH = db.Column(db.String(100), nullable=False)
  ACTIVE = db.Column(db.String(1), nullable=False, server_default='A')
  GUID_TOKEN = db.Column(db.String(150), nullable=False)
  GUID_EXPIRE = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())
  CREATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())
  UPDATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())


auth_keys = ['USER_ID', 'SALT', 'PASSWORD_HASH', 'GUID_TOKEN']