
def test_get_all_books_with_no_records(client):
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
        "description": "Covered with craters",
        "miles from sun": "40 million"
    }


def test_get_one_planet_no_data(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {'message': 'Planet 1 not found'}


def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "Where we are",
        "miles from sun": "92 million"
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"

# `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including
def test_data_fixtures(client, two_saved_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Mercury",
        "description": "Covered with craters",
        "miles from sun": "40 million"
    }, 
    {
        "id": 2,
        "name":"Venus",
        "description": "Considered Earth's twin",
        "miles_from_sun": "67 million"
    }]