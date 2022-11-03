def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_planet_by_id(client, two_saved_planets):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name": "Jupiter",
        "description": "big planet",
        "moons": 80
    }

def test_get_planet_by_id_not_found(client, two_saved_planets):
    response = client.get("planets/6")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message":f"Planet 6 not found"}