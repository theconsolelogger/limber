"""create apikey table

Revision ID: 5fe0a2e9cc1d
Revises: 27be053abfe3
Create Date: 2020-08-09 16:04:53.150627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fe0a2e9cc1d'
down_revision = '27be053abfe3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'apikey',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False),
        sa.Column('key', sa.String(64), nullable=False)
    )

def downgrade():
    op.drop_table('apikey')
