"""Add union tables

Revision ID: dfbf1a787e6b
Revises: 3361888597f4
Create Date: 2022-03-09 02:01:43.821932

"""

# revision identifiers, used by Alembic.
revision = "dfbf1a787e6b"
down_revision = "3361888597f4"
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "unions",
        sa.Column(
            "union_id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("created_by", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("administrator", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("(now() at time zone 'utc')"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("(now() at time zone 'utc')"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["administrator"],
            ["users.user_id"],
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["users.user_id"],
        ),
        sa.PrimaryKeyConstraint("union_id"),
        sa.UniqueConstraint("union_id"),
    )
    op.create_index(
        op.f("ix_unions_administrator"), "unions", ["administrator"], unique=False
    )
    op.create_table(
        "union_users",
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("union_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("(now() at time zone 'utc')"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("(now() at time zone 'utc')"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["union_id"], ["unions.union_id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.user_id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "union_id"),
    )
    op.add_column("users", sa.Column("email", sa.String()))
    op.execute("UPDATE users SET email = '' WHERE email IS NULL")
    op.alter_column("users", "updated_at", nullable=False)
    op.alter_column(
        "users",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text("timezone('utc'::text, now())"),
    )
    op.create_unique_constraint(None, "users", ["user_id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    op.alter_column(
        "users",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
        existing_server_default=sa.text("timezone('utc'::text, now())"),
    )
    op.drop_column("users", "email")
    op.drop_table("union_users")
    op.drop_index(op.f("ix_unions_administrator"), table_name="unions")
    op.drop_table("unions")
    # ### end Alembic commands ###
