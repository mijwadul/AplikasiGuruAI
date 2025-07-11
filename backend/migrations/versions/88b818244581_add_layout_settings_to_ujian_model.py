"""Add layout settings to Ujian model

Revision ID: 88b818244581
Revises: 8a95c5ccf7e4
Create Date: 2025-07-10 22:05:45.822437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88b818244581'
down_revision = '8a95c5ccf7e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ujian', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pengaturan_layout', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ujian', schema=None) as batch_op:
        batch_op.drop_column('pengaturan_layout')

    # ### end Alembic commands ###
