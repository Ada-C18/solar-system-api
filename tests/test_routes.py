def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_returns_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "The smallest planet",
        "radius": 1516
    }

def test_get_one_planet_no_fixture(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message" : "Planet 1 not found"
    }

def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body[0] == {
        "id": 1,
        "name": "Mercury",
        "description": "The smallest planet",
        "radius": 1516
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Venus",
        "description": "The second planet from the Sun and Earth's closest planetary neighbor",
        "radius": 3760
    }

    assert len(response_body) == 2

def test_create_planet_creates_planet(client):

    #Act
    EXPECTED_PLANET = {"name": "Earth",
        "description": "The third planet from the Sun and the only astronomical object known to harbor life",
        "radius": 3958}

    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_json()


    #Assert
    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"