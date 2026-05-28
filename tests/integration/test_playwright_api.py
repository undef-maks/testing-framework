
def test_playwright_get(api_request_context):
    response = api_request_context.get("/posts/1")
    assert response.status == 200
    assert response.ok
    
    data = response.json()
    assert data["userId"] == 1

def test_playwright_post(api_request_context):
    response = api_request_context.post(
        "/posts",
        data={
            "title": "playwright post",
            "body": "learning api testing",
            "userId": 42
        }
    )
    assert response.status == 201
    assert response.json()["title"] == "playwright post"
