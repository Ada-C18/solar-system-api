import pytest

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

## Writing Tests

# Create test fixtures and unit tests for the following test cases:

# 1. `GET` `/planets/1` returns a response body that matches our fixture
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

# 1. `GET` `/planets/1` with no data in test database (no fixture) returns a `404`
# 1. `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including appropriate test data
# 1. `POST` `/planets` with a JSON request body returns a `201`