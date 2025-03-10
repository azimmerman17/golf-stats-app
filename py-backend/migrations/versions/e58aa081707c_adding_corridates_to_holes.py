"""Adding corridates to holes

Revision ID: e58aa081707c
Revises: 1f44bf2fb5ce
Create Date: 2025-03-06 17:43:43.597754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e58aa081707c'
down_revision = '1f44bf2fb5ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hole', schema=None) as batch_op:
        batch_op.add_column(sa.Column('TEE_LAT_LON', sa.ARRAY(sa.Float(), dimensions=2), nullable=True))
        batch_op.add_column(sa.Column('DL_LAT_LON', sa.ARRAY(sa.Float(), dimensions=2), nullable=True))
        batch_op.add_column(sa.Column('DL2_LAT_LON', sa.ARRAY(sa.Float(), dimensions=2), nullable=True))
        batch_op.add_column(sa.Column('GREEN_LAT_LON', sa.ARRAY(sa.Float(), dimensions=2), nullable=True))
        batch_op.add_column(sa.Column('GREEN_DEPTH', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('ZOOM', sa.Integer(), nullable=True))

    with op.batch_alter_table('hole', schema=None) as batch_op:
        batch_op.create_check_constraint('HEADING_HOLE_MIN', sa.sql.column('HEADING') >= 0)
        batch_op.create_check_constraint('HEADING_HOLE_MAX', sa.sql.column('HEADING') <= 360)
        batch_op.create_check_constraint('ZOOM_MIN', sa.sql.column('ZOOM') >= 0)
        batch_op.create_check_constraint('ZOOM_MAX', sa.sql.column('ZOOM') <= 360)

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hole', schema=None) as batch_op:
        batch_op.create_index('fki_hole_TEE_ID_fkey', ['TEE_ID'], unique=False)
        batch_op.drop_column('ZOOM')
        batch_op.drop_column('GREEN_DEPTH')
        batch_op.drop_column('GREEN_LAT_LON')
        batch_op.drop_column('DL2_LAT_LON')
        batch_op.drop_column('DL_LAT_LON')
        batch_op.drop_column('TEE_LAT_LON')

    # ### end Alembic commands ###
