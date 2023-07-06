"""empty message

Revision ID: 5f57c9f6c349
Revises: 94fef19abf5b
Create Date: 2023-07-05 23:55:40.306726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f57c9f6c349'
down_revision = '94fef19abf5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campers', schema=None) as batch_op:
        batch_op.drop_constraint('uq_campers_camper_name', type_='unique')
        batch_op.create_unique_constraint(batch_op.f('uq_campers_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campers', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_campers_username'), type_='unique')
        batch_op.create_unique_constraint('uq_campers_camper_name', ['camper_name'])

    # ### end Alembic commands ###
