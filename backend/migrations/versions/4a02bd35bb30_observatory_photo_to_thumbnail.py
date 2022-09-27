"""Observatory.photo to thumbnail

Revision ID: 4a02bd35bb30
Revises: f545b345135c
Create Date: 2022-09-27 13:03:47.075429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a02bd35bb30'
down_revision = 'f545b345135c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_observatory', sa.Column('thumbnail', sa.String(), nullable=True))
    op.execute("UPDATE geopaysages.t_observatory set thumbnail = photo")
    op.drop_column('t_observatory', 'photo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_observatory', sa.Column('photo', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('t_observatory', 'thumbnail')
    # ### end Alembic commands ###
