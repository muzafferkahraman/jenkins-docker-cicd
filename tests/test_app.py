from app.main import app

def test_app():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
