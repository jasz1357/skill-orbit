from __future__ import annotations

import hashlib
import math
import re
from collections import Counter

import httpx

from app.core.config import settings
from app.services.semantic_intents import expand_text_with_intents


_ALIASES: dict[str, tuple[str, ...]] = {
    "ppt": ("ppt", "presentation", "slides", "deck", "gamma", "beautiful.ai", "演示", "幻灯片", "汇报"),
    "演示": ("ppt", "presentation", "slides", "deck", "gamma", "beautiful.ai", "汇报"),
    "演示文档": ("ppt", "presentation", "slides", "deck", "gamma", "beautiful.ai", "汇报", "提案"),
    "演示稿": ("ppt", "presentation", "slides", "deck", "gamma", "beautiful.ai", "汇报", "提案"),
    "幻灯": ("ppt", "presentation", "slides", "deck", "gamma", "beautiful.ai"),
    "汇报": ("ppt", "report", "presentation", "slides", "deck", "gamma"),
    "报告": ("report", "research", "presentation", "slides", "ppt", "研报"),
    "代码": ("code", "coding", "cursor", "claude code", "github", "编程"),
    "编程": ("code", "coding", "cursor", "claude code", "github"),
    "视频": ("video", "runway", "veo", "kling", "剪辑"),
    "图片": ("image", "visual", "midjourney", "recraft", "canva", "设计"),
    "设计": ("design", "visual", "canva", "figma", "recraft"),
    "研究": ("research", "perplexity", "notebooklm", "paper", "报告"),
    "搜索": ("search", "research", "perplexity", "genspark"),
    "自动化": ("automation", "workflow", "agent", "n8n", "make"),
    "客服": ("support", "zendesk", "intercom", "rag", "客户"),
    "营销": ("marketing", "campaign", "seo", "copywriting", "增长"),
}


class EmbeddingClient:
    def __init__(self) -> None:
        self.provider = settings.embedding_provider.strip().lower() or "local"
        self.dimension = settings.embedding_dimension
        self.model = settings.openai_embedding_model if self.provider == "openai" else f"local-hash-{self.dimension}"

    def embed(self, text: str) -> list[float]:
        expanded_text = expand_text_with_intents(text)
        if self.provider == "openai" and settings.openai_api_key:
            return self._embed_openai(expanded_text)
        return local_hash_embedding(expanded_text, self.dimension)

    def _embed_openai(self, text: str) -> list[float]:
        response = httpx.post(
            "https://api.openai.com/v1/embeddings",
            headers={"Authorization": f"Bearer {settings.openai_api_key}"},
            json={"model": settings.openai_embedding_model, "input": text},
            timeout=30,
        )
        response.raise_for_status()
        return response.json()["data"][0]["embedding"]


def local_hash_embedding(text: str, dimension: int) -> list[float]:
    tokens = _tokenize(text)
    if not tokens:
        return [0.0] * dimension

    counts = Counter(tokens)
    vector = [0.0] * dimension
    for token, count in counts.items():
        digest = hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest()
        raw = int.from_bytes(digest, "big")
        index = raw % dimension
        sign = 1.0 if raw & 1 else -1.0
        vector[index] += sign * (1.0 + math.log(count))

    norm = math.sqrt(sum(value * value for value in vector))
    if norm == 0:
        return vector
    return [value / norm for value in vector]


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if not left or not right or len(left) != len(right):
        return 0.0
    return sum(a * b for a, b in zip(left, right))


def _tokenize(text: str) -> list[str]:
    lowered = text.lower()
    tokens: list[str] = []
    tokens.extend(re.findall(r"[a-z0-9][a-z0-9.+#/-]*", lowered))

    cjk = re.findall(r"[\u4e00-\u9fff]", text)
    tokens.extend(cjk)
    tokens.extend("".join(pair) for pair in zip(cjk, cjk[1:]))
    tokens.extend("".join(cjk[index : index + 3]) for index in range(max(0, len(cjk) - 2)))

    for trigger, aliases in _ALIASES.items():
        if trigger.lower() in lowered or trigger in text:
            tokens.extend(aliases)
    return tokens
