from app.models.planet import Planet

def test_get_all_planets_with_empty_db_return_empty_list(client):

    response = client.get('/planets')
    response_body = response.get_json()

    assert response_body == []
    assert response.status_code == 200

def test_get_one_planet(client,two_saved_planets):

    response = client.get('/planets/2')
    response_body = response.get_json()

    planet2 = {
        'id':2,
        'name': 'Blorp',
        'color': 'Purple',
        'description': 'Stinky'
    }

    assert response.status_code == 200
    assert response_body == planet2

def test_no_data_return_failure(client):

    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404

def test_return_array(client):
# Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
    {
            "id": 1,
            "name": 'Dink',
            "color": 'Green',
            "description": 'Fluffy'
        },
    {
            "id": 2,
            "name": 'Blorp',
            "color": 'Purple',
            "description": 'Stinky'
        },
    {
            "id": 3,
            "name": 'Florpus',
            "color": 'Red',
            "description": 'Shy'
        }
    ]

def test_request_body_json(client):
# Act
    response = client.post("/planets", json={
        "name": "Cripper"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    
    assert Planet.query.all() == []




# 1. `GET` `/planets/1` returns a response body that matches our fixture
# 1. `GET` `/planets/1` with no data in test database (no fixture) returns a `404`
# 1. `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including appropriate test data
# 1. `POST` `/planets` with a JSON request body returns a `201`