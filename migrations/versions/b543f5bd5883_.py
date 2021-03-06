"""empty message

Revision ID: b543f5bd5883
Revises:
Create Date: 2017-10-16 00:43:39.690820

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = 'b543f5bd5883'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'movie',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'showing',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),
        sa.Column('website', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('phone', sa.String(), nullable=True),
        sa.Column(
            'geometry',
            geoalchemy2.types.Geography(
                geometry_type='POLYGON', srid=4326, spatial_index=False),
            nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(
        'idx_showing_geometry', 'showing', ['geometry'],
        unique=False, postgresql_using='gist')
    op.create_table(
        'movie_showing',
        sa.Column('movie_id', sa.BigInteger(), nullable=False),
        sa.Column('showing_id', sa.BigInteger(), nullable=False),
        sa.Column('time_from', sa.DateTime(), nullable=True),
        sa.Column('time_to', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
        sa.ForeignKeyConstraint(['showing_id'], ['showing.id'], ),
        sa.PrimaryKeyConstraint('movie_id', 'showing_id')
    )
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_showing')
    op.drop_index('idx_showing_geometry', table_name='showing')
    op.drop_table('showing')
    op.drop_table('movie')
    # ### end Alembic commands ###


def upgrade_admin():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'admin',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_admin():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    # ### end Alembic commands ###
