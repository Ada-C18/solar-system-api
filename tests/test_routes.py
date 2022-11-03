from flask import jsonify
from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    #act
    response = client.get('/planets')
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == []


# GET /planets/1 returns response body that matches our fixture
def test_get_first_planet(client, one_planet):
# act
    response = client.get('/planets/1')
    response_body = response.get_json()
# assert
    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["flag"] == one_planet.flag

# GET /planets/1 with no data in test database (no fixture) returns a 404
def test_get_empty_database_returns_404(client):
# act
    response = client.get('/planets/1')
# assert
    assert response.status_code == 404

# GET /planets with JSON request body returns a 200
# def test_planets_with_data_return_200_with_valid_data(client, multi_planets):
# # act
#     response = client.get('/planets')
#     response_body = response.get_json()
# # assert
#     assert response.status_code == 200
#     assert response_body["id"] == multi_planets[0].id
#     assert response_body["name"] == one_planet.name
#     assert response_body["description"] == one_planet.description
#     assert response_body["flag"] == one_planet.flag


# POST /planets with JSON request body returns a 201
def test_save_planet(client):
    # arrange
    NEW_PLANET ={"name": "Mercury", 
                    "description": "planet closest to the sun.", 
                    "flag": False}
    # act
    response = client.post('/planets', json=NEW_PLANET)
    response_body = response.get_json()
    
    # assert
    assert response.status_code == 201
    assert response_body == f"planet {NEW_PLANET['name']} successfully created!"