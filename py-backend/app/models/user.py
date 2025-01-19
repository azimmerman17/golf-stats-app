from datetime import datetime, date

from app.extensions import db, orm
from app.models.facility import FACILITY

# Model Contains Profile Information for Users
class USER(db.Model):
  USER_ID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  USERNAME = db.Column(db.String(25), nullable=False, unique=True)
  EMAIL = db.Column(db.String(50), nullable=False, unique=True)
  GENDER = db.Column(db.Enum('M','F','N','P', name='USER_GENDER'), nullable=False, server_default='P')
  DOB = db.Column(db.DATE, nullable=False, default=date.today())
  PLAYER_TYPE = db.Column(db.Enum('A','C','P','TP', name='USER_TYPE'), nullable=False, server_default='A')
  HOME_FACILITY = db.Column(db.Integer, db.ForeignKey(FACILITY.FACILITY_ID, onupdate="CASCADE", ondelete="CASCADE"), nullable=True)
  NATIONALITY = db.Column(db.String(3))
  UNITS = db.Column(db.Enum('Y','M', name='USER_UNITS'), nullable=False, server_default='Y')
  ROLE = db.Column(db.Enum('basic','vip','admin', name='USER_ROLE'), nullable=False, server_default='basic')
  CREATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())
  UPDATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())

  def __init__(self, USER_ID, USERNAME, EMAIL, GENDER, NATIONALITY, PLAYER_TYPE, UNITS, HOME_FACILITY, DOB):
    self['USER_ID'] = USER_ID
    self['USERNAME'] = USERNAME
    self['EMAIL'] = EMAIL
    self['GENDER'] = GENDER
    self['NATIONALITY'] = NATIONALITY
    self['PLAYER_TYPE'] = PLAYER_TYPE
    self['UNITS'] = UNITS
    self['HOME_FACILITY'] = HOME_FACILITY
    self['DOB'] = DOB

    print('self',self)

    # return self
