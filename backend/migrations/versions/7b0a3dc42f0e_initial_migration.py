"""Initial migration..

Revision ID: 7b0a3dc42f0e
Revises: 
Create Date: 2022-05-31 11:17:47.169182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b0a3dc42f0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('villes_france',
    sa.Column('ville_id', sa.Integer(), server_default=FetchedValue(), nullable=False),
    sa.Column('ville_departement', sa.String(), nullable=True),
    sa.Column('ville_slug', sa.String(), nullable=True),
    sa.Column('ville_nom', sa.String(), nullable=True),
    sa.Column('ville_nom_simple', sa.String(), nullable=True),
    sa.Column('ville_nom_reel', sa.String(), nullable=True),
    sa.Column('ville_nom_soundex', sa.String(), nullable=True),
    sa.Column('ville_nom_metaphone', sa.String(), nullable=True),
    sa.Column('ville_code_postal', sa.String(), nullable=True),
    sa.Column('ville_commune', sa.String(), nullable=True),
    sa.Column('ville_code_commune', sa.String(), nullable=True),
    sa.Column('ville_arrondissement', sa.Integer(), nullable=True),
    sa.Column('ville_canton', sa.String(), nullable=True),
    sa.Column('ville_amdi', sa.Integer(), nullable=True),
    sa.Column('ville_population_2010', sa.Integer(), nullable=True),
    sa.Column('ville_population_1999', sa.Integer(), nullable=True),
    sa.Column('ville_population_2012', sa.Integer(), nullable=True),
    sa.Column('ville_densite_2010', sa.Integer(), nullable=True),
    sa.Column('ville_surface', sa.Integer(), nullable=True),
    sa.Column('ville_longitude_deg', sa.Integer(), nullable=True),
    sa.Column('ville_latitude_deg', sa.Integer(), nullable=True),
    sa.Column('ville_longitude_grd', sa.String(), nullable=True),
    sa.Column('ville_latitude_grd', sa.String(), nullable=True),
    sa.Column('ville_latitude_dms', sa.String(), nullable=True),
    sa.Column('ville_zmin', sa.Integer(), nullable=True),
    sa.Column('ville_zmax', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ville_id'),
    schema='geopaysages'
    )
    op.alter_column('conf', 'key',
               existing_type=sa.VARCHAR(),
               nullable=False,
               schema='geopaysages')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('conf', 'key',
               existing_type=sa.VARCHAR(),
               nullable=True,
               schema='geopaysages')
    op.drop_table('villes_france', schema='geopaysages')
    # ### end Alembic commands ###
