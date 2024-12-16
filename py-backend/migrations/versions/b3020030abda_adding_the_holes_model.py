"""Adding the holes model

Revision ID: b3020030abda
Revises: 8b8ac6403f3a
Create Date: 2024-12-14 15:08:59.714252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3020030abda'
down_revision = '8b8ac6403f3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hole',
    sa.Column('HOLE_ID', sa.Integer(), nullable=False),
    sa.Column('TEE_ID', sa.Integer(), nullable=False),
    sa.Column('NUMBER', sa.Integer(), nullable=False),
    sa.Column('YARDS', sa.Integer(), nullable=False, server_default=400),
    sa.Column('METERS', sa.Integer(), nullable=False, server_default=367),
    sa.Column('PAR_MALE', sa.Integer(), nullable=True),
    sa.Column('SI_MALE', sa.Integer(), nullable=True),
    sa.Column('PAR_FEMALE', sa.Integer(), nullable=True),
    sa.Column('SI_FEMALE', sa.Integer(), nullable=True),
    sa.Column('EFFECTIVE_DATE', sa.DATE(), nullable=False),
    sa.Column('CREATED_AT', sa.TIMESTAMP(), nullable=False),
    sa.Column('UPDATED_AT', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['TEE_ID'], ['tee.TEE_ID'], ),
    sa.PrimaryKeyConstraint('HOLE_ID')
    )
    with op.batch_alter_table('hole', schema=None) as batch_op:
        batch_op.create_check_constraint('CHECK_HOLE_NUM_MIN', sa.sql.column('NUMBER') > 0)
        batch_op.create_check_constraint('CHECK_HOLE_NUM_MAX', sa.sql.column('NUMBER') <= 18)
        batch_op.create_check_constraint('CHECK_HOLE_YARDS_MIN', sa.sql.column('YARDS') > 0)
        batch_op.create_check_constraint('CHECK_HOLE_YARDS_MAX', sa.sql.column('YARDS') <= 999)
        batch_op.create_check_constraint('CHECK_HOLE_METERS_MIN', sa.sql.column('METERS') > 0)
        batch_op.create_check_constraint('CHECK_HOLE_METERS_MAX', sa.sql.column('METERS') <= 999)
        batch_op.create_check_constraint('CHECK_HOLE_METERS_YARDS', sa.sql.column('METERS') < sa.sql.column('YARDS'))
        batch_op.create_check_constraint('CHECK_HOLE_PAR_M_MIN', sa.sql.column('PAR_MALE') > 2)
        batch_op.create_check_constraint('CHECK_HOLE_PAR_M_MAX', sa.sql.column('PAR_MALE') <= 6)
        batch_op.create_check_constraint('CHECK_HOLE_SI_M_MIN', sa.sql.column('SI_MALE') > 0)
        batch_op.create_check_constraint('CHECK_HOLE_SI_M_MAX', sa.sql.column('SI_MALE') <= 18)
        batch_op.create_check_constraint('CHECK_HOLE_PAR_F_MIN', sa.sql.column('PAR_FEMALE') > 2)
        batch_op.create_check_constraint('CHECK_HOLE_PAR_F_MAX', sa.sql.column('PAR_FEMALE') <= 6)
        batch_op.create_check_constraint('CHECK_HOLE_SI_F_MIN', sa.sql.column('SI_FEMALE') > 0)
        batch_op.create_check_constraint('CHECK_HOLE_SI_F_MAX', sa.sql.column('SI_FEMALE') <= 18)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hole')
    # ### end Alembic commands ###
