"""Separate into file, matrix

Revision ID: 9a218c7df2ac
Revises: fc7aef9b17f8
Create Date: 2021-02-26 15:17:07.083450

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "9a218c7df2ac"
down_revision = "fc7aef9b17f8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "f64_matrix",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "time_created",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column(
            "time_updated",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("content", sa.ARRAY(sa.FLOAT()), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "file",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "time_created",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column(
            "time_updated",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("filename", sa.String(), nullable=False),
        sa.Column("mimetype", sa.String(), nullable=False),
        sa.Column("content", sa.LargeBinary(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("record", sa.Column("f64_matrix_id", sa.Integer(), nullable=True))
    op.add_column("record", sa.Column("file_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "record", "file", ["file_id"], ["id"])
    op.create_foreign_key(None, "record", "f64_matrix", ["f64_matrix_id"], ["id"])
    op.drop_column("record", "data")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "record",
        sa.Column("data", postgresql.BYTEA(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, "record", type_="foreignkey")
    op.drop_constraint(None, "record", type_="foreignkey")
    op.drop_column("record", "file_id")
    op.drop_column("record", "f64_matrix_id")
    op.drop_table("file")
    op.drop_table("f64_matrix")
    # ### end Alembic commands ###
