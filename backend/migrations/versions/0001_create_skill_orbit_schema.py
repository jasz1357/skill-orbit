"""create skill orbit schema

Revision ID: 0001_create_skill_orbit_schema
Revises:
Create Date: 2026-05-04
"""

from datetime import datetime, timezone

from alembic import op
import sqlalchemy as sa

revision = "0001_create_skill_orbit_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "categories",
        sa.Column("id", sa.String(length=48), primary_key=True),
        sa.Column("label", sa.String(length=32), nullable=False),
        sa.Column("label_cn", sa.String(length=32), nullable=False, server_default=""),
        sa.Column("color", sa.String(length=7), nullable=False),
        sa.Column("radius", sa.Float(), nullable=False),
        sa.Column("tilt_x", sa.Float(), nullable=False),
        sa.Column("tilt_y", sa.Float(), nullable=False),
        sa.Column("tilt_z", sa.Float(), nullable=False),
        sa.Column("speed", sa.Float(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_table(
        "skills",
        sa.Column("id", sa.String(length=48), primary_key=True),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.Column("category_id", sa.String(length=48), sa.ForeignKey("categories.id", ondelete="RESTRICT"), nullable=False),
        sa.Column("note", sa.Text(), nullable=False, server_default=""),
        sa.Column("source_text", sa.Text(), nullable=True),
        sa.Column("angle", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_skills_category_id", "skills", ["category_id"])
    op.create_index("ix_skills_created_at", "skills", ["created_at"])

    now = datetime.now(timezone.utc)
    op.bulk_insert(
        sa.table(
            "categories",
            sa.column("id", sa.String),
            sa.column("label", sa.String),
            sa.column("label_cn", sa.String),
            sa.column("color", sa.String),
            sa.column("radius", sa.Float),
            sa.column("tilt_x", sa.Float),
            sa.column("tilt_y", sa.Float),
            sa.column("tilt_z", sa.Float),
            sa.column("speed", sa.Float),
            sa.column("created_at", sa.DateTime),
            sa.column("updated_at", sa.DateTime),
        ),
        [
            {"id": "craft", "label": "CRAFT", "label_cn": "", "color": "#ffb066", "radius": 1.55, "tilt_x": 0.3, "tilt_y": 0.1, "tilt_z": 0.05, "speed": 0.06, "created_at": now, "updated_at": now},
            {"id": "theory", "label": "THEORY", "label_cn": "", "color": "#7ed6e6", "radius": 1.95, "tilt_x": -0.55, "tilt_y": 0.4, "tilt_z": 0.2, "speed": 0.04, "created_at": now, "updated_at": now},
            {"id": "life", "label": "LIFE", "label_cn": "", "color": "#e69aa3", "radius": 2.4, "tilt_x": 0.8, "tilt_y": -0.3, "tilt_z": 0.1, "speed": 0.03, "created_at": now, "updated_at": now},
        ],
    )
    op.bulk_insert(
        sa.table(
            "skills",
            sa.column("id", sa.String),
            sa.column("name", sa.String),
            sa.column("category_id", sa.String),
            sa.column("note", sa.Text),
            sa.column("source_text", sa.Text),
            sa.column("angle", sa.Float),
            sa.column("created_at", sa.DateTime),
            sa.column("updated_at", sa.DateTime),
        ),
        [
            {"id": "seed_css_grid_subgrid", "name": "CSS Grid subgrid layout", "category_id": "craft", "note": "", "source_text": None, "angle": None, "created_at": now, "updated_at": now},
            {"id": "seed_use_reducer", "name": "useReducer for complex form state", "category_id": "craft", "note": "", "source_text": None, "angle": None, "created_at": now, "updated_at": now},
            {"id": "seed_cipher_basics", "name": "Caesar and substitution cipher basics", "category_id": "theory", "note": "", "source_text": None, "angle": None, "created_at": now, "updated_at": now},
            {"id": "seed_sandwich", "name": "Japanese sandwich technique", "category_id": "life", "note": "", "source_text": None, "angle": None, "created_at": now, "updated_at": now},
            {"id": "seed_fract_shader", "name": "fract in WebGL shaders", "category_id": "craft", "note": "", "source_text": None, "angle": None, "created_at": now, "updated_at": now},
            {"id": "seed_bayes", "name": "Intuition for Bayesian inference", "category_id": "theory", "note": "", "source_text": None, "angle": None, "created_at": now, "updated_at": now},
            {"id": "seed_coffee_temp", "name": "Water temperature curve in coffee brewing", "category_id": "life", "note": "", "source_text": None, "angle": None, "created_at": now, "updated_at": now},
        ],
    )


def downgrade() -> None:
    op.drop_index("ix_skills_created_at", table_name="skills")
    op.drop_index("ix_skills_category_id", table_name="skills")
    op.drop_table("skills")
    op.drop_table("categories")
