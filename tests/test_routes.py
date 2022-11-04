from app.models.planet import Planet

def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    #act
    response = client.get("/planets")

    #assert
    assert response.status_code == 200
    assert response.get_json() == []