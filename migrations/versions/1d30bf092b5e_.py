"""empty message

Revision ID: 1d30bf092b5e
Revises: eacc67e48bd4
Create Date: 2021-04-15 22:23:47.841115

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1d30bf092b5e'
down_revision = 'eacc67e48bd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('make', sa.String(length=25), nullable=True),
    sa.Column('model', sa.String(length=50), nullable=True),
    sa.Column('colour', sa.String(length=25), nullable=True),
    sa.Column('year', sa.String(length=4), nullable=True),
    sa.Column('transmission', sa.String(length=25), nullable=True),
    sa.Column('car_type', sa.String(length=25), nullable=True),
    sa.Column('photo', sa.String(length=150), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
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
    op.drop_table('favourites')
    op.drop_table('user_profiles')
    op.drop_table('cars')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('make', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('model', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('colour', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('year', sa.VARCHAR(length=4), autoincrement=False, nullable=True),
    sa.Column('transmission', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('car_type', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('photo', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='cars_pkey')
    )
    op.create_table('user_profiles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('biography', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
    sa.Column('photo', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('date_joined', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_profiles_pkey'),
    sa.UniqueConstraint('username', name='user_profiles_username_key')
    )
    op.create_table('favourites',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('car_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='favourites_pkey')
    )
    op.drop_table('Users')
    op.drop_table('Favourites')
    op.drop_table('Cars')
    # ### end Alembic commands ###
