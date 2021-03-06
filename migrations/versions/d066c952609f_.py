"""empty message

Revision ID: d066c952609f
Revises: 148ca5b1356a
Create Date: 2017-10-21 17:06:34.870839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd066c952609f'
down_revision = '148ca5b1356a'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'showing', sa.Column('last_modified', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('showing', 'last_modified')
    # ### end Alembic commands ###


def upgrade_admin():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_admin():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
