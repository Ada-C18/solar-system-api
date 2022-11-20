def test_get_all_planets_empty_db_returns_none(client):
    # Act
    response = client.get("/planets")

    # Assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_one_planet_returns_seeded_planet(client, one_saved_planet):
    # Act
    response = client.get(f"/planets/{one_saved_planet.id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["id"] == one_saved_planet.id
    assert response_body["name"] == one_saved_planet.name
    assert response_body["description"] == one_saved_planet.description
    assert response_body["color"] == one_saved_planet.color

def test_get_one_planet_empty_db_returns_404(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404
    assert response.get_json() == {"message": "Planet 1 not found"}

def test_get_two_planets_returns_seeded_planets(client, two_saved_planets):
    # Act
    response = client.get(f"/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2

def test_create_one_planet(client):
    # Act
    EXPECTED_PLANET = {
        "name": "Captain Planet", 
        "description": "a super planet", 
        "color": "red and blue"
    }

    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Captain Planet successfully created."

