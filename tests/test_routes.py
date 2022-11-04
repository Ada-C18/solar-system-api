def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Mercury",
        "description": "Smallest planet in our solar system",
        "moon_count": 0
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Venus",
        "description": "Hottest planet in our solar system",
        "moon_count": 0
    }

def test_get_all_planets_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_create_planet(client):
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "That's us!",
        "moon_count": 1
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"