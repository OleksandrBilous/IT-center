"""Initial migration.

Revision ID: 361740f8f88d
Revises: 284acb530e51
Create Date: 2023-01-09 16:31:18.390943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '361740f8f88d'
down_revision = '284acb530e51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=64), nullable=False))
        batch_op.add_column(sa.Column('Surname', sa.String(length=64), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('Surname')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
