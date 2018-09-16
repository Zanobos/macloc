"""empty message

Revision ID: e32f62a85382
Revises: ddecaf68f3a4
Create Date: 2018-09-16 12:34:15.300788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e32f62a85382'
down_revision = 'ddecaf68f3a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record', sa.Column('z', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('record', 'z')
    # ### end Alembic commands ###
