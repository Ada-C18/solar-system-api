
import pytest

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# `GET` `/planets/1` returns a response body that matches our fixture
def test_get_one_planet(client, one_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {'color': 'green', 'description': 'Very testy', 'id': 1, 'name': 'Planet_Test'}


# `GET` `/planets/1` with no data in test database (no fixture) returns a `404`
def test_get_one_planet_with_no_fixture(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404 
    assert response_body == {"message": "planet 1 not found"}


# `GET` `/planets` with valid test data (fixtures) returns a `200` 
# with an array including appropriate test data
def test_get_all_planets(client, two_saved_planets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{'color': 'green', 'description': 'Very testy', 'id': 1, 'name': 'Planet_Test'},{'color': 'green 2', 'description': 'Very testy 2', 'id': 2, 'name': 'Planet_Test_2'}]

#  `POST` `/planets` with a JSON request body returns a `201`
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "test_planet_3",
        "description": "description 3",
        "color": "color 3"
    })
    response_body = response.get_json() 

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet test_planet_3 successfully created"



