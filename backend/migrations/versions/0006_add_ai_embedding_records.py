"""add ai embedding records

Revision ID: 0006_add_ai_embedding_records
Revises: 0005_add_ai_subskills
Create Date: 2026-05-20 20:20:00.000000
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "0006_add_ai_embedding_records"
down_revision: Union[str, None] = "0005_add_ai_subskills"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ai_embedding_records",
        sa.Column("id", sa.String(length=120), nullable=False),
        sa.Column("source_id", sa.String(length=120), nullable=False),
        sa.Column("source_type", sa.String(length=24), nullable=False),
        sa.Column("title", sa.String(length=180), nullable=False),
        sa.Column("category_id", sa.String(length=48), nullable=False, server_default=""),
        sa.Column("category_label", sa.String(length=80), nullable=False, server_default=""),
        sa.Column("sub_skill_id", sa.String(length=64), nullable=False, server_default=""),
        sa.Column("sub_skill_label", sa.String(length=80), nullable=False, server_default=""),
        sa.Column("content", sa.Text(), nullable=False, server_default=""),
        sa.Column("embedding_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("metadata_json", sa.Text(), nullable=False, server_default="{}"),
        sa.Column("content_hash", sa.String(length=64), nullable=False),
        sa.Column("embedding_provider", sa.String(length=32), nullable=False, server_default="local"),
        sa.Column("embedding_model", sa.String(length=80), nullable=False, server_default="local-hash"),
        sa.Column("embedding_dimension", sa.Integer(), nullable=False, server_default="384"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_ai_embedding_records_source", "ai_embedding_records", ["source_type", "source_id"], unique=True)
    op.create_index("ix_ai_embedding_records_source_type", "ai_embedding_records", ["source_type"])
    op.create_index("ix_ai_embedding_records_category_id", "ai_embedding_records", ["category_id"])
    op.create_index("ix_ai_embedding_records_sub_skill_id", "ai_embedding_records", ["sub_skill_id"])
    op.create_index("ix_ai_embedding_records_content_hash", "ai_embedding_records", ["content_hash"])


def downgrade() -> None:
    op.drop_index("ix_ai_embedding_records_content_hash", table_name="ai_embedding_records")
    op.drop_index("ix_ai_embedding_records_sub_skill_id", table_name="ai_embedding_records")
    op.drop_index("ix_ai_embedding_records_category_id", table_name="ai_embedding_records")
    op.drop_index("ix_ai_embedding_records_source_type", table_name="ai_embedding_records")
    op.drop_index("ix_ai_embedding_records_source", table_name="ai_embedding_records")
    op.drop_table("ai_embedding_records")
