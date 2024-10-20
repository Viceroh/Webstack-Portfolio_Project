"""dropped code column

Revision ID: 9790cec59339
Revises: fc2151ced564
Create Date: 2024-10-16 13:11:33.913475

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9790cec59339'
down_revision = 'fc2151ced564'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.drop_column('code')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('code', mysql.VARCHAR(length=255), nullable=True))

    # ### end Alembic commands ###
