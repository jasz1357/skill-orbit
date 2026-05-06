from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import CategoryRecord, SkillRecord

DEFAULT_CATEGORIES = [
    {"id": "craft", "label": "CREATE", "label_cn": "", "color": "#ffb066", "radius": 1.55, "tilt_x": 0.3, "tilt_y": 0.1, "tilt_z": 0.05, "speed": 0.06},
    {"id": "theory", "label": "ANALYZE", "label_cn": "", "color": "#7ed6e6", "radius": 1.95, "tilt_x": -0.55, "tilt_y": 0.4, "tilt_z": 0.2, "speed": 0.04},
    {"id": "life", "label": "AUTOMATE", "label_cn": "", "color": "#e69aa3", "radius": 2.4, "tilt_x": 0.8, "tilt_y": -0.3, "tilt_z": 0.1, "speed": 0.03},
]

DEFAULT_SKILLS = [
    ("seed_css_grid_subgrid", "CSS Grid subgrid layout", "craft"),
    ("seed_use_reducer", "useReducer for complex form state", "craft"),
    ("seed_cipher_basics", "Caesar and substitution cipher basics", "theory"),
    ("seed_sandwich", "Japanese sandwich technique", "life"),
    ("seed_fract_shader", "fract in WebGL shaders", "craft"),
    ("seed_bayes", "Intuition for Bayesian inference", "theory"),
    ("seed_coffee_temp", "Water temperature curve in coffee brewing", "life"),
]


def seed_defaults(db: Session) -> None:
    for payload in DEFAULT_CATEGORIES:
        exists = db.get(CategoryRecord, payload["id"])
        if not exists:
            db.add(CategoryRecord(**payload))
            continue
        # Keep user-custom labels; only auto-migrate known old defaults.
        if exists.label in {"CRAFT", "THEORY", "LIFE"}:
            exists.label = payload["label"]

    for skill_id, name, category_id in DEFAULT_SKILLS:
        exists = db.get(SkillRecord, skill_id)
        if not exists:
            db.add(SkillRecord(id=skill_id, name=name, category_id=category_id))

    db.commit()
