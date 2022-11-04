def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Saturn",
        "surface_area": 123890491,
        "moons": 83,
        "distance_from_sun": 123123123123,
        "namesake": "The Roman god of time",
    }


def test_create_one_planet(client):
    # Act
    response = client.post(
        "/planets",
        json={
            "id": 9,
            "name": "Pluto",
            "surface_area": 123890491,
            "moons": 0,
            "distance_from_sun": 123123123123,
            "namesake": "The Roman god of the underworld",
        },
    )
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet successfully created"
