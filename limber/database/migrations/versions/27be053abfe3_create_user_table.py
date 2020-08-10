"""create user table

Revision ID: 27be053abfe3
Revises: 87324732c8bb
Create Date: 2020-08-09 16:01:52.646984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27be053abfe3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String(200), nullable=False)
    )


def downgrade():
    op.drop_table('user')
