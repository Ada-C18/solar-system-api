

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# `GET` `/planets/1` returns a response body that matches our fixture
def test_get_one_planet(client):
    raise Exception
    # pass


# `GET` `/planets/1` with no data in test database (no fixture) returns a `404`
def test_get_one_planet_with_no_fixture(client):
    raise Exception
    # pass


# `GET` `/planets` with valid test data (fixtures) returns a `200` 
# with an array including appropriate test data
def test_get_all_planets(client):
    raise Exception
    # pass

#  `POST` `/planets` with a JSON request body returns a `201`
def test_create_one_planet(client):
    raise Exception
    # pass



