"""add ai recommendation feedback

Revision ID: 0007_add_ai_recommendation_feedback
Revises: 0006_add_ai_embedding_records
Create Date: 2026-05-21 11:20:00.000000
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


revision: str = "0007_add_ai_recommendation_feedback"
down_revision: Union[str, None] = "0006_add_ai_embedding_records"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ai_recommendation_feedback",
        sa.Column("id", sa.String(length=48), nullable=False),
        sa.Column("user_id", sa.String(length=48), nullable=True),
        sa.Column("query", sa.Text(), nullable=False, server_default=""),
        sa.Column("source_id", sa.String(length=120), nullable=False),
        sa.Column("source_type", sa.String(length=24), nullable=False),
        sa.Column("plan_type", sa.String(length=40), nullable=False, server_default=""),
        sa.Column("rating", sa.String(length=24), nullable=False),
        sa.Column("comment", sa.Text(), nullable=False, server_default=""),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_ai_recommendation_feedback_source", "ai_recommendation_feedback", ["source_type", "source_id"])
    op.create_index("ix_ai_recommendation_feedback_user_id", "ai_recommendation_feedback", ["user_id"])
    op.create_index("ix_ai_recommendation_feedback_rating", "ai_recommendation_feedback", ["rating"])
    op.create_index("ix_ai_recommendation_feedback_created_at", "ai_recommendation_feedback", ["created_at"])


def downgrade() -> None:
    op.drop_index("ix_ai_recommendation_feedback_created_at", table_name="ai_recommendation_feedback")
    op.drop_index("ix_ai_recommendation_feedback_rating", table_name="ai_recommendation_feedback")
    op.drop_index("ix_ai_recommendation_feedback_user_id", table_name="ai_recommendation_feedback")
    op.drop_index("ix_ai_recommendation_feedback_source", table_name="ai_recommendation_feedback")
    op.drop_table("ai_recommendation_feedback")
