"""Create Subscription table

Revision ID: 687d307ef486
Revises: 
Create Date: 2024-10-03 00:29:28.813738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '687d307ef486'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('date', sa.String(length=500), nullable=False),
    sa.Column('body', sa.String(length=250), nullable=False),
    sa.Column('author', sa.String(length=250), nullable=False),
    sa.Column('img_url', sa.String(length=500), nullable=False),
    sa.Column('subtitle', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('register',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=69), nullable=True),
    sa.Column('password', sa.VARCHAR(length=69), nullable=True),
    sa.Column('name', sa.VARCHAR(length=69), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('register')
    op.drop_table('blog')
    # ### end Alembic commands ###
