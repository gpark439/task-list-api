"""empty message

Revision ID: d72b7b7d248f
Revises: 1da967f7b911
Create Date: 2022-05-05 19:27:44.746781

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd72b7b7d248f'
down_revision = '1da967f7b911'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_complete', sa.Boolean(), nullable=True))
    op.alter_column('task', 'completed_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'completed_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('task', 'is_complete')
    # ### end Alembic commands ###
