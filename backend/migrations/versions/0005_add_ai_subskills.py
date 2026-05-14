"""add ai sub skill classification

Revision ID: 0005_add_ai_subskills
Revises: 0004_add_ai_library_items
Create Date: 2026-05-13 22:55:00.000000
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "0005_add_ai_subskills"
down_revision: Union[str, None] = "0004_add_ai_library_items"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ai_subskills",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("category_id", sa.String(length=48), nullable=False),
        sa.Column("category_label", sa.String(length=80), nullable=False),
        sa.Column("label", sa.String(length=80), nullable=False),
        sa.Column("label_cn", sa.String(length=80), nullable=False, server_default=""),
        sa.Column("sort_order", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_ai_subskills_category_id", "ai_subskills", ["category_id"])

    op.add_column("ai_skills", sa.Column("sub_skill_id", sa.String(length=64), nullable=False, server_default=""))
    op.add_column("ai_skills", sa.Column("sub_skill_label", sa.String(length=80), nullable=False, server_default=""))
    op.create_index("ix_ai_skills_sub_skill_id", "ai_skills", ["sub_skill_id"])

    op.add_column("ai_library_items", sa.Column("sub_skill_id", sa.String(length=64), nullable=False, server_default=""))
    op.add_column("ai_library_items", sa.Column("sub_skill_label", sa.String(length=80), nullable=False, server_default=""))
    op.create_index("ix_ai_library_items_sub_skill_id", "ai_library_items", ["sub_skill_id"])


def downgrade() -> None:
    op.drop_index("ix_ai_library_items_sub_skill_id", table_name="ai_library_items")
    op.drop_column("ai_library_items", "sub_skill_label")
    op.drop_column("ai_library_items", "sub_skill_id")

    op.drop_index("ix_ai_skills_sub_skill_id", table_name="ai_skills")
    op.drop_column("ai_skills", "sub_skill_label")
    op.drop_column("ai_skills", "sub_skill_id")

    op.drop_index("ix_ai_subskills_category_id", table_name="ai_subskills")
    op.drop_table("ai_subskills")
