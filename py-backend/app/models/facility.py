from datetime import datetime, date

from app.extensions import db, orm

# Model Contains Profile Information for Facilities
class FACILITY(db.Model):
  FACILITY_ID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  NAME = db.Column(db.String(100), nullable=False)
  HANDLE = db.Column(db.String(25), nullable=False, unique=True)
  CLASSIFICATION = db.Column(db.Enum('D','P','R','M','S','O', name='FACILITY_CLASSIFICATION'), nullable=False, server_default='O')
  COURSE_COUNT = db.Column(db.Integer, db.CheckConstraint('COURSE_COUNT > 0', name='CHECK_COURSE_COUNT'), nullable=False, server_default='1')
  ESTABLISHED = db.Column(db.Integer, db.CheckConstraint('ESTABLISHED > 1400', name='CHECK_ESTABLISHED_MIN'))
  WEBSITE = db.Column(db.String(100))
  ADDRESS = db.Column(db.String(100))
  CITY = db.Column(db.String(50))
  STATE = db.Column(db.String(3))
  COUNTRY = db.Column(db.String(3))
  GEO_LAT = db.Column(db.FLOAT, db.CheckConstraint('GEO_LAT > -90', name='CHECK_GEO_LAT_MIN'), db.CheckConstraint('GEO_LAT < 90', name='CHECK_GEO_LAT_MAX'))
  GEO_LON = db.Column(db.FLOAT, db.CheckConstraint('GEO_LON > -180', name='CHECK_GEO_LON_MIN'), db.CheckConstraint('GEO_LON < 180', name='CHECK_GEO_LON_MAX'))
  CREATED_AT = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())
  UPDATED_AT = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())

  @orm.validates('COURSE_COUNT')
  def validate_course_count(self, key, value):
    if value <= 0:
      raise ValueError(f'Invalid Course Count - {value} - A facility must have a course')
    return value

  @orm.validates('ESTABLISHED')
  def validate_established(self, key, value):
    if value < 1400:
      raise ValueError(f'Invalid Facility Established Year - {value} - The first writen record of golf is from 1457 and the first modern day course was esablished in 1574, please sumbit a later date.')
    elif value > date.today().year:
      raise ValueError(f'Invalid Facility Established Year - {value} - Facilities cannot have a future dated established year, it is likely this facility is still under construction, please resumbit this facility once it opens.')
    return value

  @orm.validates('GEO_LAT')
  def validate_geo_lat(self, key, value):
    if not -90 < value < 90:
      raise ValueError(f'Invalid Facility Latitude - {value} - The maximum and minimun latitude values on Earth is +/- 90 degrees, please check and resubmit your coordinates')
    return value

  @orm.validates('GEO_LON')
  def validate_geo_lon(self, key, value):
    if not -180 < value < 180:
      raise ValueError(f'Invalid Facility Longitude - {value} - The maximum and minimun longitude values on Earth is +/- 180 degrees, please check and resubmit your coordinates')
    return value

  def __init__(self, FACILITY_ID, NAME, HANDLE, CLASSIFICATION, COURSE_COUNT, ESTABLISHED, WEBSITE, ADDRESS, CITY, STATE, COUNTRY, GEO_LAT, GEO_LON):
    self['FACILITY_ID'] = FACILITY_ID
    self['NAME'] = NAME
    self['HANDLE'] = HANDLE
    self['CLASSIFICATION'] = CLASSIFICATION
    self['COURSE_COUNT'] = COURSE_COUNT
    self['ESTABLISHED'] = ESTABLISHED
    self['WEBSITE'] = WEBSITE
    self['ADDRESS'] = ADDRESS
    self['CITY'] = CITY
    self['STATE'] = STATE
    self['COUNTRY'] = COUNTRY
    self['GEO_LAT'] = GEO_LAT
    self['GEO_LON'] = GEO_LON

    print('self',self)

    # return self

# list of keys for a SQL insert statement
facility_keys = ['FACILITY_ID', 'NAME', 'HANDLE', 'CLASSIFICATION', 'COURSE_COUNT', 'ESTABLISHED', 'WEBSITE', 'ADDRESS', 'CITY', 'STATE', 'COUNTRY', 'GEO_LAT', 'GEO_LON']
# list of keys that are marked 'Not Null' and do not have a default value
facility_not_null = ['FACILITY_ID', 'NAME', 'HANDLE']


