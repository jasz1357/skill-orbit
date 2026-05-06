"""add auth users

Revision ID: 0002_add_auth_users
Revises: 0001_create_skill_orbit_schema
Create Date: 2026-05-04
"""

from alembic import op
import sqlalchemy as sa

revision = "0002_add_auth_users"
down_revision = "0001_create_skill_orbit_schema"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.String(length=48), primary_key=True),
        sa.Column("username", sa.String(length=64), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("is_admin", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_users_username", "users", ["username"], unique=True)
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.add_column("skills", sa.Column("user_id", sa.String(length=48), nullable=True))
    op.create_index("ix_skills_user_id", "skills", ["user_id"])


def downgrade() -> None:
    op.drop_index("ix_skills_user_id", table_name="skills")
    op.drop_column("skills", "user_id")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_users_username", table_name="users")
    op.drop_table("users")
