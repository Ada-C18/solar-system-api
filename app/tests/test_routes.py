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
        "name": "Ocean Planet",
        "description": "watr 4evr",
        "diameter": "0 miles"
    }

def test_get_one_planet_with_no_data(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 1 not found"}

def test_get_one_planet_with_invalid_id(client):
    # Act
    response = client.get("/planets/**")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet ** invalid"}

def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Ocean Planet",
        "description": "watr 4evr",
        "diameter": "0 miles"
    },
    {
        "id": 2,
        "name": "Mountain Planet",
        "description": "i luv 2 climb rocks",
        "diameter": "1 mile"
    }]
    assert len(response_body) == 2

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "The Best!",
        "diameter": "5 miles"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet New Planet successfully created"