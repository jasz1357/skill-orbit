from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
from datetime import datetime, timedelta, timezone
from typing import Optional

from app.core.config import settings


def hash_password(password: str, salt: Optional[bytes] = None) -> str:
    salt = salt or os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000)
    return f"pbkdf2_sha256${_b64(salt)}${_b64(digest)}"


def verify_password(password: str, password_hash: str) -> bool:
    try:
        algo, salt_b64, digest_b64 = password_hash.split("$", 2)
        if algo != "pbkdf2_sha256":
            return False
        salt = _unb64(salt_b64)
        expected = _unb64(digest_b64)
        actual = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000)
        return hmac.compare_digest(actual, expected)
    except ValueError:
        return False


def create_access_token(subject: str) -> str:
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    payload = {"sub": subject, "exp": int(expires_at.timestamp())}
    body = _b64(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    sig = _sign(body)
    return f"{body}.{sig}"


def verify_access_token(token: str) -> Optional[str]:
    try:
        body, sig = token.split(".", 1)
        if not hmac.compare_digest(_sign(body), sig):
            return None
        payload = json.loads(_unb64(body))
        if int(payload["exp"]) < int(datetime.now(timezone.utc).timestamp()):
            return None
        return str(payload["sub"])
    except (ValueError, KeyError, json.JSONDecodeError):
        return None


def _sign(body: str) -> str:
    digest = hmac.new(settings.auth_secret_key.encode("utf-8"), body.encode("utf-8"), hashlib.sha256).digest()
    return _b64(digest)


def _b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def _unb64(data: str) -> bytes:
    padded = data + "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(padded.encode("ascii"))
