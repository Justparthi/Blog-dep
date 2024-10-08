"""Create Subscription table

Revision ID: b56839e752c8
Revises: 1459768496e3
Create Date: 2024-10-03 00:39:58.369119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b56839e752c8'
down_revision = '1459768496e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.VARCHAR(length=10000),
               type_=sa.String(length=1000000),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.String(length=1000000),
               type_=sa.VARCHAR(length=10000),
               existing_nullable=False)

    # ### end Alembic commands ###
