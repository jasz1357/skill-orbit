from fastapi.testclient import TestClient

from app.main import app


def test_health_check() -> None:
    with TestClient(app) as client:
        response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_ai_compose_finds_ppt_workflow_stack() -> None:
    with TestClient(app) as client:
        response = client.post("/api/v1/ai-skills/compose", json={"query": "我今天想做一个 PPT", "top_k": 5})

    assert response.status_code == 200
    payload = response.json()
    assert payload["recommendations"]
    combined_text = " ".join(
        f"{item['title']} {item['summary']} {' '.join(item['tools'])}"
        for item in payload["recommendations"]
    ).lower()
    assert "ppt" in combined_text or "presentation" in combined_text or "gamma" in combined_text


def test_ai_compose_treats_ppt_and_presentation_doc_as_same_intent() -> None:
    with TestClient(app) as client:
        ppt_response = client.post("/api/v1/ai-skills/compose", json={"query": "我想做 PPT", "top_k": 3})
        deck_response = client.post("/api/v1/ai-skills/compose", json={"query": "我想做演示文档", "top_k": 3})

    assert ppt_response.status_code == 200
    assert deck_response.status_code == 200
    ppt_ids = [item["source_id"] for item in ppt_response.json()["recommendations"]]
    deck_ids = [item["source_id"] for item in deck_response.json()["recommendations"]]
    assert ppt_ids == deck_ids


def test_ai_recommend_returns_ranked_ppt_plans() -> None:
    with TestClient(app) as client:
        response = client.post("/api/v1/ai-skills/recommend", json={"query": "我想做一个给客户看的 PPT", "top_k": 3})

    assert response.status_code == 200
    payload = response.json()
    assert "presentation_deck" in payload["intent_ids"]
    assert len(payload["plans"]) == 3
    assert all(plan["reason"] for plan in payload["plans"])
    combined_titles = " ".join(plan["recommendation"]["title"].lower() for plan in payload["plans"])
    assert "ppt" in combined_titles or "presentation" in combined_titles or "deck" in combined_titles


def test_hot_ai_seed_adds_current_tool_cards() -> None:
    with TestClient(app) as client:
        response = client.get("/api/v1/ai-skills", params={"q": "DeepSeek", "limit": 20})

    assert response.status_code == 200
    tool_ids = {item["id"] for item in response.json()}
    assert "deepseek-reasoning-coding" in tool_ids


def test_hot_ai_library_surfaces_video_ad_stack() -> None:
    with TestClient(app) as client:
        response = client.get("/api/v1/ai-skills/library", params={"q": "Veo Runway Kling CapCut", "limit": 20})

    assert response.status_code == 200
    item_ids = {item["id"] for item in response.json()}
    assert "combo-video-ad-factory" in item_ids
