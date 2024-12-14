from datetime import datetime

from app.extensions import db, orm
from app.models.facility import FACILITY

from datetime import datetime

from app.extensions import db, orm
from app.models.facility import FACILITY

# Model Contains Profile Information for Courses
# Facilities with multiple Courses should have Multiple Course Rows
class COURSE(db.Model):
  COURSE_ID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  FACILITY_ID = db.Column(db.Integer, db.ForeignKey(FACILITY.FACILITY_ID), nullable=False)
  NAME = db.Column(db.String(50))
  HOLE_COUNT = db.Column(db.Integer, db.CheckConstraint('HOLE_CRSE_COUNT >= 1 AND HOLE_COUNT <= 18'), nullable=False, server_default='18')
  ESTABLISHED = db.Column(db.Integer, db.CheckConstraint('ESTABLISHED > 1400', name='CHECK_CRSE_ESTABLISHED_MIN'))
  ARCHITECT = db.Column(db.String(100))
  CREATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())
  UPDATED_AT = db.Column(db.TIMESTAMP,nullable=False, default=datetime.now())

  @orm.validates('HOLE_COUNT')
  def validate_hole_count(self, key, value):
    if not 0 < value < 18:
      raise ValueError(f'Invalid Hole Count - {value}')
    return value

  @orm.validates('ESTABLISHED')
  def validate_established(self, key, value):
    if value < 1574:
      raise ValueError(f'Invalid Course Established Year - {value} - The first modern day course was esablished in 1574, please sumbit a later date.')
    elif value > date.today().year:
      raise ValueError(f'Invalid Course Established Year - {value} - Courses cannot have a future dated established year, it is likely this facility is still under construction, please resumbit this course once it opens.')
    return value

def __init__(self, COURSE_ID, FACILITY_ID, NAME, HOLE_COUNT, ESTABLISHED, ARCHITECT):
  self.COURSE_ID = COURSE_ID
  self.FACILITY_ID = FACILITY_ID
  self.NAME = NAME
  self.HOLE_COUNT = HOLE_COUNT
  self.ESTABLISHED = ESTABLISHED
  self.ARCHITECT = ARCHITECT

  return self
