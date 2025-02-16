"""Edit menu name constraint to unique

Revision ID: 418303f5238e
Revises: 96cb76d4b49b
Create Date: 2020-02-14 01:26:54.715645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '418303f5238e'
down_revision = '96cb76d4b49b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'menu', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'menu', type_='unique')
    # ### end Alembic commands ###
