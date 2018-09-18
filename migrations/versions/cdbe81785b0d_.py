"""empty message

Revision ID: cdbe81785b0d
Revises: e32f62a85382
Create Date: 2018-09-18 12:43:17.100677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdbe81785b0d'
down_revision = 'e32f62a85382'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wall', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wall', 'active')
    # ### end Alembic commands ###
