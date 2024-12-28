from datetime import datetime, date

from app.extensions import db, orm
from app.models.tee import TEE

# Model Contains Information for each course hole
class Hole(db.Model):
  HOLE_ID = db.Column(db.Integer, primary_key=True)
  TEE_ID = db.Column(db.Integer, db.ForeignKey(TEE.TEE_ID, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  NUMBER = db.Column(db.Integer, db.CheckConstraint('NUMBER >= 1 AND NUMBER <= 18'), nullable=False)
  YARDS = db.Column(db.Integer, db.CheckConstraint('YARDS > 0 AND YARDS <= 999'), nullable=False, server_default='400')
  METERS = db.Column(db.Integer, db.CheckConstraint('METERS > 0 AND METERS <= 999'), nullable=False, server_default='367')
  PAR_MALE = db.Column(db.Integer, db.CheckConstraint('PAR_MALE >= 3 AND PAR_MALE <= 6'))
  SI_MALE = db.Column(db.Integer, db.CheckConstraint('SI_MALE >= 1 AND SI_MALE <= 18'))
  PAR_FEMALE = db.Column(db.Integer, db.CheckConstraint('PAR_FEMALE >= 3 AND PAR_FEMALE <= 6'))
  SI_FEMALE = db.Column(db.Integer, db.CheckConstraint('SI_FEMALE >= 1 AND SI_FEMALE <= 18'))
  EFFECTIVE_DATE = db.Column(db.DATE, nullable=False, default=date.today())
  CREATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())
  UPDATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())

  @orm.validates('NUMBER')
  def validate_number(self, key, value):
      if not 1 <= value <= 18:
        raise ValueError(f'Invalid Hole Number - {value} - Hole Number must be between 1 and 18')
      return value

  @orm.validates('YARDS')
  def validate_yards(self, key, value):
      if not 0 <= value <= 999:
        raise ValueError(f'Invalid Yards - {value} - Length(yds) must be between 1 and 999')
      return value

  @orm.validates('METERS')
  def validate_meters(self, key, value):
      if not 0 <= value <= 999:
        raise ValueError(f'Invalid Meters - {value} - Length(m) must be between 1 and 999')
      return value

  @orm.validates('PAR_MALE')
  @orm.validates('PAR_FEMALE')
  def validate_hole_par(self, key, value):
      if not 3 <= value <= 6:
        raise ValueError(f'Invalid Hole Par - {value} - Par must be between 3 and 6 for a hole')
      return value

  @orm.validates('SI_MALE')
  @orm.validates('SI_FEMALE')
  def validate_hole_si(self, key, value):
      if not 1 <= value <= 18:
        raise ValueError(f'Invalid Stroke Index - {value} - Stroke Index must be between 1 and 18 for a hole')
      return value

def __init__(self, HOLE_ID, TEE_ID, NUMBER, YARDS, METERS, PAR_MALE, SI_MALE, PAR_FEMALE, SI_FEMALE, EFFECTIVE_DATE):
  self.HOLE_ID = HOLE_ID
  self.TEE_ID = TEE_ID
  self.NUMBER = NUMBER
  self.YARDS = YARDS
  self.METERS = METERS
  self.PAR_MALE = PAR_MALE
  self.SI_MALE = SI_MALE
  self.PAR_FEMALE = PAR_FEMALE
  self.SI_FEMALE = SI_FEMALE
  self.EFFECTIVE_DATE = EFFECTIVE_DATE

  return self

# list of keys for a SQL insert statement
hole_keys = ['TEE_ID', 'NUMBER', 'YARDS', 'METERS', 'PAR_MALE', 'SI_MALE', 'PAR_FEMALE', 'SI_FEMALE']
# list of keys that are marked 'Not Null' and do not have a default value
hole_not_null = ['TEE_ID', 'NUMBER']