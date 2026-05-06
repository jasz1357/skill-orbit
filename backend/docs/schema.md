# Skill Orbit Database Schema

## categories

Stores orbit rings shown in the left archive panel.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `varchar(48)` | Primary key, frontend category id such as `craft` |
| `label` | `varchar(32)` | Display label, usually uppercase |
| `label_cn` | `varchar(32)` | Optional Chinese label |
| `color` | `varchar(7)` | Hex color such as `#ffb066` |
| `radius` | `float` | Orbit radius |
| `tilt_x` | `float` | Ring x-axis tilt |
| `tilt_y` | `float` | Ring y-axis tilt |
| `tilt_z` | `float` | Ring z-axis tilt |
| `speed` | `float` | Base orbit speed |
| `created_at` | `datetime` | UTC creation time |
| `updated_at` | `datetime` | UTC update time |

## skills

Stores memory nodes shown as stars on orbit rings.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `varchar(48)` | Primary key |
| `user_id` | `varchar(48)` | Owner user id |
| `name` | `varchar(80)` | Skill node title |
| `category_id` | `varchar(48)` | Foreign key to `categories.id` |
| `note` | `text` | User note from the detail editor |
| `source_text` | `text` | Original chat/input text, optional |
| `angle` | `float` | Optional frontend orbit angle |
| `created_at` | `datetime` | UTC creation time |
| `updated_at` | `datetime` | UTC update time |

## Indexes

- `ix_skills_category_id` for filtering nodes by ring.
- `ix_skills_user_id` for filtering nodes by owner.
- `ix_skills_created_at` for recent-node ordering.

## users

Stores accounts for backend mode.

| Column | Type | Notes |
| --- | --- | --- |
| `id` | `varchar(48)` | Primary key |
| `username` | `varchar(64)` | Unique username |
| `email` | `varchar(255)` | Unique email |
| `password_hash` | `varchar(255)` | PBKDF2 password hash |
| `is_admin` | `boolean` | Default admin marker |
| `created_at` | `datetime` | UTC creation time |
| `updated_at` | `datetime` | UTC update time |
