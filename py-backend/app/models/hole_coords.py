from datetime import datetime, date

from app.extensions import db, orm
from app.models.course import COURSE

# Model Contains Information for GPS Coordinated for each hole
class HOLE_COORDS(db.Model):
  HOLE_GEO_ID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  COURSE_ID = db.Column(db.Integer, db.ForeignKey(COURSE.COURSE_ID, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  NUMBER = db.Column(db.Integer, db.CheckConstraint('NUMBER >= 1', name='CHECK_COORDS_NUMBER_MIN'), db.CheckConstraint('NUMBER <= 18', name='CHECK_COORDS_NUMBER_MAX'), nullable=False)
  HANDLE = db.Column(db.String(25), nullable=False, unique=True)
  TEE_LAT = db.Column(db.FLOAT, db.CheckConstraint('TEE_LAT > -90', name='CHECK_TEE_LAT_MIN'), db.CheckConstraint('TEE_LAT < 90', name='CHECK_TEE_LAT_MAX'))
  TEE_LON = db.Column(db.FLOAT, db.CheckConstraint('TEE_LON > -180', name='CHECK_TEE_LON_MIN'), db.CheckConstraint('TEE_LON < 180', name='CHECK_TEE_LON_MAX'))
  DL_LAT = db.Column(db.FLOAT, db.CheckConstraint('DL_LAT > -90', name='CHECK_DL_LAT_MIN'), db.CheckConstraint('DL_LAT < 90', name='CHECK_DL_LAT_MAX'))
  DL_LON = db.Column(db.FLOAT, db.CheckConstraint('DL_LON > -180', name='CHECK_DL_LON_MIN'), db.CheckConstraint('DL_LON < 180', name='CHECK_DL_LON_MAX'))
  DL2_LAT = db.Column(db.FLOAT, db.CheckConstraint('DL2_LAT > -90', name='CHECK_DL2_LAT_MIN'), db.CheckConstraint('DL2_LAT < 90', name='CHECK_DL2_LAT_MAX'))
  DL2_LON = db.Column(db.FLOAT, db.CheckConstraint('DL2_LON > -180', name='CHECK_DL2_LON_MIN'), db.CheckConstraint('DL2_LON < 180', name='CHECK_DL2_LON_MAX'))
  CGREEN_LAT = db.Column(db.FLOAT, db.CheckConstraint('CGREEN_LAT > -90', name='CHECK_CGREEN_LAT_MIN'), db.CheckConstraint('CGREEN_LAT < 90', name='CHECK_CGREEN_LAT_MAX'))
  CGREEN_LON = db.Column(db.FLOAT, db.CheckConstraint('CGREEN_LON > -180', name='CHECK_CGREEN_LON_MIN'), db.CheckConstraint('CGREEN_LON < 180', name='CHECK_CGREEN_LON_MAX'))
  FGREEN_LAT = db.Column(db.FLOAT, db.CheckConstraint('FGREEN_LAT > -90', name='CHECK_FGREEN_LAT_MIN'), db.CheckConstraint('FGREEN_LAT < 90', name='CHECK_FGREEN_LAT_MAX'))
  FGREEN_LON = db.Column(db.FLOAT, db.CheckConstraint('FGREEN_LON > -180', name='CHECK_FGREEN_LON_MIN'), db.CheckConstraint('FGREEN_LON < 180', name='CHECK_FGREEN_LON_MAX'))
  BGREEN_LAT = db.Column(db.FLOAT, db.CheckConstraint('BGREEN_LAT > -90', name='CHECK_BGREEN_LAT_MIN'), db.CheckConstraint('BGREEN_LAT < 90', name='CHECK_BGREEN_LAT_MAX'))
  BGREEN_LON = db.Column(db.FLOAT, db.CheckConstraint('BGREEN_LON > -180', name='CHECK_BGREEN_LON_MIN'), db.CheckConstraint('BGREEN_LON < 180', name='CHECK_BGREEN_LON_MAX'))
  ZOOM = db.Column(db.Integer, db.CheckConstraint('ZOOM >= 1', name='CHECK_COORDS_ZOOM_MIN'), db.CheckConstraint('ZOOM <= 20', name='CHECK_COORDS_ZOOM_MAX'))
  ROTATION = db.Column(db.FLOAT, db.CheckConstraint('ROTATION >= 0', name='CHECK_ROTATION_MIN'), db.CheckConstraint('ROTATION < 360', name='CHECK_ROTATION_MAX'))
  GREEN_DEPTH = db.Column(db.FLOAT)
  CREATED_AT = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())
  UPDATED_AT = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())

  @orm.validates('NUMBER')
  def validate_number(self, key, value):
    if not 0 < value <= 18:
      raise ValueError(f'Invalid Hole Number - {value} - A hole number must be between 1 and 18')
    return value

  @orm.validates('ZOOM')
  def validate_zoom(self, key, value):
    if not 0 < value <= 18:
      raise ValueError(f'Invalid Zoom - {value} - Mapping API requires a zoom between 1 and 20')
    return value
  
  @orm.validates('ROTATION')
  def validate_zoom(self, key, value):
    if not 0 <= value < 360:
      raise ValueError(f'Invalid Rotation - {value} - Rotation value must me between 0 and 360')
    return value

  @orm.validates('GEO_LAT')
  @orm.validates('TEE_LAT')
  @orm.validates('DL_LAT')
  @orm.validates('DL2_LAT')
  @orm.validates('CGREEN_LAT')
  @orm.validates('FGREEN_LAT')
  @orm.validates('BGREEN_LAT')
  def validate_latatude(self, key, value):
    if not -90 < value < 90:
      raise ValueError(f'Invalid Latitude Value - {key}: {value} - The maximum and minimun latitude values on Earth is +/- 90 degrees, please check and resubmit your coordinates')
    return value

  @orm.validates('GEO_LON')
  @orm.validates('TEE_LON')
  @orm.validates('DL_LON')
  @orm.validates('DL2_LON')
  @orm.validates('CGREEN_LON')
  @orm.validates('FGREEN_LON')
  @orm.validates('BGREEN_LON')
  def validate_lon(self, key, value):
    if not -180 < value < 180:
      raise ValueError(f'Invalid Longitude Value - {key}: {value} - The maximum and minimun longitude values on Earth is +/- 180 degrees, please check and resubmit your coordinates')
    return value

  def __init__(self,HOLE_GEO_ID, COURSE_ID, NUMBER, HANDLE, TEE_LAT, TEE_LON, DL_LAT, DL_LON, DL2_LAT, DL2_LON, CGREEN_LAT, CGREEN_LON, FGREEN_LAT, FGREEN_LON, BGREEN_LAT, BGREEN_LON, ZOOM, ROTATION, GREEN_DEPTH):
    self.HOLE_GEO_ID = HOLE_GEO_ID
    self.COURSE_ID = COURSE_ID
    self.NUMBER = NUMBER
    self.HANDLE = HANDLE
    self.TEE_LAT = TEE_LAT
    self.TEE_LON = TEE_LON
    self.DL_LAT = DL_LAT
    self.DL_LON = DL_LON
    self.DL2_LAT = DL2_LAT
    self.DL2_LON = DL2_LON
    self.CGREEN_LAT = CGREEN_LAT
    self.CGREEN_LON = CGREEN_LON
    self.FGREEN_LAT = FGREEN_LAT
    self.FGREEN_LON = FGREEN_LON
    self.BGREEN_LAT = BGREEN_LAT
    self.BGREEN_LON = BGREEN_LON
    self.ZOOM = ZOOM
    self.ROTATION = ROTATION
    self.GREEN_DEPTH = GREEN_DEPTH

    return self