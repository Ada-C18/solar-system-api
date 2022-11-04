def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets(client,two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2


def test_get_one_planet(client,two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name":"Ocean Planet", 
        "description": "watr 4evr planet", 
        "temperature" : 1000}

def test_get_one_planet_no_fixture(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name":"Ocean Planet", 
        "description": "watr 4evr planet", 
        "temperature" : 1000}
    )
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 201
    assert response_body == "Planet Ocean Planet successfully created"

# def test_update_one_planet
