"""empty message

Revision ID: 35b9cc67c552
Revises: c7a9d081b2d0
Create Date: 2021-04-25 20:20:10.413750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35b9cc67c552'
down_revision = 'c7a9d081b2d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Favourites', 'car_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Favourites', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('Favourites', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Favourites', sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Favourites_id_seq"\'::regclass)'), autoincrement=True, nullable=False))
    op.alter_column('Favourites', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Favourites', 'car_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
