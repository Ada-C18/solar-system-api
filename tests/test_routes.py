def test_get_all_planets_with_no_records(client):
    #act
    response = client.get('/planets')
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == []


# GET /planets/1 returns response body that matches our fixture
def test_get_first_planet(client):
# act
    response = client.get('/planets/1')
    response_body = response.get_json()
# assert
    assert response.status_code == 200
    assert response_body == {
        "id": "1",
        "name": ""

    }

# GET /planets/1 with no data in test database (no fixture) returns a 404

# act

# assert

# GET /planets with JSON request body returns a 201

# act

# assert