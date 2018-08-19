"""walls table

Revision ID: 59c9624d1730
Revises: 
Create Date: 2018-08-19 20:10:15.947706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59c9624d1730'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wall',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('width', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wall')
    # ### end Alembic commands ###