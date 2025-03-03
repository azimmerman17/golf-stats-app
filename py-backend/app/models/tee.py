from datetime import datetime, date

from app.extensions import db, orm
from app.models.course import COURSE

# Model Contains Information for Courses Tees
class TEE(db.Model):
  TEE_ID = db.Column(db.Integer, primary_key=True)
  COURSE_ID = db.Column(db.Integer, db.ForeignKey(COURSE.COURSE_ID, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  NAME = db.Column(db.String, nullable=False)
  YARDS = db.Column(db.Integer, db.CheckConstraint('YARDS > 0'), nullable=False, server_default='7200')
  METERS = db.Column(db.Integer, db.CheckConstraint('METERS > 0'), nullable=False, server_default='6600')
  HOLE_COUNT = db.Column(db.Integer, db.CheckConstraint('HOLE_COUNT >= 1 AND HOLE_COUNT <= 18'), nullable=False, server_default='18')
  CREATED_AT = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())
  UPDATED_AT = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())


  @orm.validates('HOLE_COUNT')
  def validate_hole_count(self, key, value):
    if not 0 < value < 18:
      raise ValueError(f'Invalid Hole Count - {value} - Courses must have a hole count between 1 to 18')
    return value

  @orm.validates('YARDS')
  def validate_yardage(self, key, value):
    if value < 0:
      raise ValueError(f'Invalid Yardage - {value} - Course must have a positive length')
    return value

  @orm.validates('METERS')
  def validate_yardage(self, key, value):
    if value < 0:
      raise ValueError(f'Invalid Yardage - {value} - Course must have a length')
    return value

def __init__(self, TEE_ID, COURSE_ID, NAME, YARDS, METERS, HOLE_COUNT):
  self.TEE_ID = TEE_ID
  self.COURSE_ID = COURSE_ID
  self.NAME = NAME
  self.YARDS = YARDS
  self.METERS = METERS
  self.HOLE_COUNT = HOLE_COUNT

  return self

# list of keys for a SQL insert statement
tee_keys = ['TEE_ID', 'COURSE_ID', 'NAME', 'YARDS', 'METERS', 'HOLE_COUNT']
# list of keys that are marked 'Not Null' and do not have a default value
tee_not_null = ['TEE_ID', 'COURSE_ID', 'NAME']
