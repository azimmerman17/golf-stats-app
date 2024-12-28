from datetime import datetime, date

from app.extensions import db, orm
from app.models.tee import TEE

# Model Contains Information for Courses Ratings
class RATING(db.Model):
  RATING_ID = db.Column(db.Integer, primary_key=True)
  TEE_ID = db.Column(db.Integer, db.ForeignKey(TEE.TEE_ID, onupdate="CASCADE", ondelete="CASCADE"))
  NAME = db.Column(db.String, nullable=False)  # FRONT, BACK, FULL, ETC
  HOLE_COUNT = db.Column(db.Integer, db.CheckConstraint('HOLE_COUNT = 9 OR HOLE_COUNT = 18'), server_default='18')
  GENDER = db.Column(db.Enum('M','F', name='COURSE_RATING_GENDER'), nullable=False, server_default='M')
  START_HOLE = db.Column(db.Integer, db.CheckConstraint('START_HOLE >= 1 AND START_HOLE <= 18 AND START_HOLE <= HOLE_COUNT'), nullable=False, server_default='1')
  COURSE_RATING = db.Column(db.FLOAT, nullable=False)
  SLOPE = db.Column(db.Integer, db.CheckConstraint('SLOPE >= 55 AND SLOPE <= 155'), nullable=False)
  PAR = db.Column(db.Integer, db.CheckConstraint('PAR >= 27 AND PAR <= 80'), nullable=False)
  BOGEY_RATING = db.Column(db.FLOAT)
  EFFECTIVE_DATE = db.Column(db.DATE, nullable=False, default=date.today())
  CREATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())
  UPDATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())

  @orm.validates('HOLE_COUNT')
  def validate_hole_count(self, key, value):
      if value != 9 or value != 18:
        raise ValueError(f'Invalid Hole Count - {value} - Invalid Hole Counts, Handicap hole counts must be 9 or 18')
      return value

  @orm.validates('START_HOLE')
  def validate_start_hole(self, key, value):
    if not 0 < value < 18:
      raise ValueError(f'Invalid Start Hole - {value} - Start Hole must be > 1 and <= 18')
    return value

  @orm.validates('SLOPE')
  def validate_slope(self, key, value):
    if not 55 <= value <= 155:
      raise ValueError(f'Invalid Slope Value - {value} - Slope Value must be between 55 and 155')
    return value

  @orm.validates('PAR')
  def validate_slope(self, key, value):
    if not 27 <= value <= 80:
      raise ValueError(f'Invalid Par Value - {value} - PAr Value must be between 27 and 80')
    return value

def __init__(self, RATING_ID, TEE_ID, NAME, HOLE_COUNT, GENDER, START_HOLE, COURSE_RATING, SLOPE, PAR, BOGEY_RATING, EFFECTIVE_DATE):
  self.RATING_ID = RATING_ID
  self.TEE_ID = TEE_ID
  self.NAME = NAME
  self.HOLE_COUNT = HOLE_COUNT
  self.GENDER = GENDER
  self.START_HOLE = START_HOLE
  self.COURSE_RATING = COURSE_RATING
  self.SLOPE = SLOPE
  self.PAR = PAR
  self.BOGEY_RATING = BOGEY_RATING
  self.EFFECTIVE_DATE = EFFECTIVE_DATE

  return self

# list of keys for a SQL insert statement
rating_keys = ['TEE_ID', 'NAME', 'HOLE_COUNT', 'GENDER', 'START_HOLE', 'COURSE_RATING', 'SLOPE', 'PAR', 'BOGEY_RATING', 'EFFECTIVE_DATE']
# list of keys that are marked 'Not Null' and do not have a default value
rating_not_null = ['TEE_ID', 'NAME', 'HOLE_COUNT', 'GENDER', 'START_HOLE', 'COURSE_RATING', 'SLOPE', 'PAR']