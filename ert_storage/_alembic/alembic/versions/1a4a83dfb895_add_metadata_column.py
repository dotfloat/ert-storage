"""Add metadata column

Revision ID: 1a4a83dfb895
Revises: bea15008ea91
Create Date: 2021-04-13 10:41:35.187857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1a4a83dfb895"
down_revision = "bea15008ea91"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("ensemble", sa.Column("metadata", sa.JSON(), nullable=True))
    op.add_column("experiment", sa.Column("metadata", sa.JSON(), nullable=True))
    op.add_column("observation", sa.Column("metadata", sa.JSON(), nullable=True))
    op.add_column("record", sa.Column("metadata", sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("record", "metadata")
    op.drop_column("observation", "metadata")
    op.drop_column("experiment", "metadata")
    op.drop_column("ensemble", "metadata")
    # ### end Alembic commands ###