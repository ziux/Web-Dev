"""empty message

Revision ID: 85426fe77f32
Revises: 6eee95d90d70
Create Date: 2018-06-19 19:10:44.254048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85426fe77f32'
down_revision = '6eee95d90d70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
