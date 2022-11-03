import pytest

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name":"Mercury",
        "description":"solid",
        "moons":0
    }

def test_get_one_planet_no_data(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {'message': 'planet 1 not found'}

def test_get_planets(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name":"Mercury",
        "description":"solid",
        "moons":0
    }
    {
        "id": 2,
        "name":"Venus",
        "description":"bright and volcanic",
        "moons":0
    }

def test_create_one_planet(client):
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "half and half",
        "moons": 1
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Earth has been created successfully"