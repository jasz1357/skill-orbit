"""add ai skill library

Revision ID: 0003_add_ai_skill_library
Revises: 0002_add_auth_users
Create Date: 2026-05-09
"""

from alembic import op
import sqlalchemy as sa

revision = "0003_add_ai_skill_library"
down_revision = "0002_add_auth_users"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "ai_skills",
        sa.Column("id", sa.String(length=80), primary_key=True),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("category_id", sa.String(length=48), nullable=False),
        sa.Column("category_label", sa.String(length=80), nullable=False),
        sa.Column("tool", sa.String(length=80), nullable=False, server_default=""),
        sa.Column("stage", sa.String(length=40), nullable=False, server_default=""),
        sa.Column("description", sa.Text(), nullable=False, server_default=""),
        sa.Column("tags_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("examples_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("input_types_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("output_types_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("difficulty", sa.Integer(), nullable=False, server_default="2"),
        sa.Column("importance", sa.Integer(), nullable=False, server_default="50"),
        sa.Column("is_core", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_ai_skills_category_id", "ai_skills", ["category_id"])
    op.create_index("ix_ai_skills_is_core", "ai_skills", ["is_core"])
    op.create_index("ix_ai_skills_importance", "ai_skills", ["importance"])


def downgrade() -> None:
    op.drop_index("ix_ai_skills_importance", table_name="ai_skills")
    op.drop_index("ix_ai_skills_is_core", table_name="ai_skills")
    op.drop_index("ix_ai_skills_category_id", table_name="ai_skills")
    op.drop_table("ai_skills")
