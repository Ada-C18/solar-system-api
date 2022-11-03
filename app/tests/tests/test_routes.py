from app.models.planet import Planet

def test_get_all_planets_with_empty_db_return_empty_list(client):
    response = client.get('/planets')

    response_body = response.get_json()

    assert response_body == []
    assert response.status_code == 200