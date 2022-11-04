from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet_with_two_records(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "name": "Saturn",
        "surface_area": 123890491,
        "moons": 83,
        "distance_from_sun": 123123123123,
        "namesake": "The Roman god of time"
    }

def test_create_one_planet(client):
    #Arrange
    EXPECTED_PLANET = {
            "name": "Pluto",
            "surface_area": 123890491,
            "moons": 0,
            "distance_from_sun": 123123123123,
            "namesake": "The Roman god of the underworld"
    }
    EXPECTED_ID = 1

    # Act
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)
    actual_planet = Planet.query.get(EXPECTED_ID)

    # Assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully added"
    