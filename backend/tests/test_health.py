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
    assert len(payload["comparison"]) == 3
    assert all(plan["reason"] for plan in payload["plans"])
    assert all(plan["execution_steps"] for plan in payload["plans"])
    assert all(plan["pros"] for plan in payload["plans"])
    combined_titles = " ".join(plan["recommendation"]["title"].lower() for plan in payload["plans"])
    assert "ppt" in combined_titles or "presentation" in combined_titles or "deck" in combined_titles


def test_ai_recommendation_feedback_is_saved() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/ai-skills/feedback",
            json={
                "query": "我想做 PPT",
                "source_id": "workflow-china-ppt-kimi-wps-ai",
                "source_type": "workflow",
                "plan_type": "fastest",
                "rating": "up",
            },
        )

    assert response.status_code == 201
    payload = response.json()
    assert payload["source_id"] == "workflow-china-ppt-kimi-wps-ai"
    assert payload["rating"] == "up"


def test_ai_advice_asks_clarifying_questions_for_vague_ppt() -> None:
    with TestClient(app) as client:
        response = client.post("/api/v1/ai-skills/advice", json={"query": "我想做 PPT", "top_k": 3})

    assert response.status_code == 200
    payload = response.json()
    assert payload["needs_clarification"] is True
    assert payload["clarification_questions"]
    assert payload["clarification_questions"][0]["options"]
    assert not payload["plans"]


def test_ai_advice_recommends_when_context_is_specific() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/ai-skills/advice",
            json={"query": "我想做一个给客户看的 PPT，我有资料，今天要，正式一点", "top_k": 3},
        )

    assert response.status_code == 200
    payload = response.json()
    assert payload["needs_clarification"] is False
    assert len(payload["plans"]) == 3
    assert payload["comparison"]


def test_ai_advice_option_choices_change_plan_order() -> None:
    with TestClient(app) as client:
        fast_response = client.post(
            "/api/v1/ai-skills/advice",
            json={"query": "我想做 PPT；给客户看；已有文档/资料；越快越好", "top_k": 3},
        )
        visual_response = client.post(
            "/api/v1/ai-skills/advice",
            json={"query": "我想做 PPT；给老板/团队看；有旧 PPT 需要美化；要好看", "top_k": 3},
        )

    assert fast_response.status_code == 200
    assert visual_response.status_code == 200
    fast_titles = [plan["recommendation"]["title"] for plan in fast_response.json()["plans"]]
    visual_titles = [plan["recommendation"]["title"] for plan in visual_response.json()["plans"]]
    assert fast_titles != visual_titles
