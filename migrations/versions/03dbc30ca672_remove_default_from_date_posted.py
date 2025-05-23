"""Remove default from date_posted

Revision ID: 03dbc30ca672
Revises: 38ff0b867918
Create Date: 2025-05-15 16:10:23.873440

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '03dbc30ca672'
down_revision = '38ff0b867918'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('date_posted',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text("'2024-01-01 00:00:00'::timestamp without time zone"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('date_posted',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text("'2024-01-01 00:00:00'::timestamp without time zone"))

    # ### end Alembic commands ###
