"""add ai library combination and workflow items

Revision ID: 0004_add_ai_library_items
Revises: 0003_add_ai_skill_library
Create Date: 2026-05-09 18:15:00.000000
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "0004_add_ai_library_items"
down_revision: Union[str, None] = "0003_add_ai_skill_library"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ai_library_items",
        sa.Column("id", sa.String(length=100), nullable=False),
        sa.Column("item_type", sa.String(length=24), nullable=False),
        sa.Column("title", sa.String(length=180), nullable=False),
        sa.Column("category_id", sa.String(length=48), nullable=False, server_default=""),
        sa.Column("category_label", sa.String(length=80), nullable=False, server_default=""),
        sa.Column("summary", sa.Text(), nullable=False, server_default=""),
        sa.Column("tools_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("steps_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("outputs_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("tags_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("source_section", sa.String(length=120), nullable=False, server_default=""),
        sa.Column("importance", sa.Integer(), nullable=False, server_default="50"),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_ai_library_items_item_type", "ai_library_items", ["item_type"])
    op.create_index("ix_ai_library_items_category_id", "ai_library_items", ["category_id"])
    op.create_index("ix_ai_library_items_importance", "ai_library_items", ["importance"])


def downgrade() -> None:
    op.drop_index("ix_ai_library_items_importance", table_name="ai_library_items")
    op.drop_index("ix_ai_library_items_category_id", table_name="ai_library_items")
    op.drop_index("ix_ai_library_items_item_type", table_name="ai_library_items")
    op.drop_table("ai_library_items")
