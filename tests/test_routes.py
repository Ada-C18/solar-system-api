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
        "name": "Mercury",
        "description": "small",
        "moons": 2
    }

def test_get_planet_with_no_data(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Ivy",
        "description": "furry!",
        "moons": 3
    })
    response_body = response.get_data(as_text=True)
    print('RESPONSE BODY:', response)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Ivy successfully created"