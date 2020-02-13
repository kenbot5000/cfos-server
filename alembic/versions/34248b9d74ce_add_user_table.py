"""add user table

Revision ID: 34248b9d74ce
Revises: 
Create Date: 2020-02-11 18:57:48.885768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34248b9d74ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), unique=True)
    )


def downgrade():
    op.drop_table('user')
