"""empty message

Revision ID: 31cb2d758e1b
Revises: 
Create Date: 2021-04-13 01:34:42.067121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31cb2d758e1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=120), nullable=True),
    sa.Column('biography', sa.String(length=1000), nullable=True),
    sa.Column('photo', sa.String(length=100), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    # ### end Alembic commands ###
