from app.models.planet import Planet

"""
TODO: 
DONE - GET planets/1 to return a response that matches our fixture
DONE - POST /planets with JSON request body and returns 201
DONE - GET planets/1 with no data in test database return 404
DONE - GET planets with test data returns 200 with array including test data
"""

def test_get_all_planets_in_database(client, saved_test_planets):
    #pass
    #act
    response = client.get('/planets')
    response_body = Planet.query.all()

    #assert
    assert response.status_code == 200

def test_no_data_in_database_for_specific_endpoint(client):
    # pass
    #act
    response = client.get('planets/3')
    response_body = response.get_json()

    #assert
    assert response.status_code == 404

def test_get_planets_when_there_are_no_records_in_database(client):
    # pass
    #act
    response = client.get('/planets')
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_by_id(client, saved_test_planets):
    # pass
    #act
    response = client.get('/planets/1')
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body == {
        'id': 1,
        'color': "pink",
        'is_dwarf': True, 
        'livability': 3, 
        'moons': 99, 
        'name': "Pretend Planet X",
    }

def test_create_one_new_planet(client):
    # pass
    #act
    EXPECTED_PLANET = {
        "color": "green",
        "is_dwarf": False, 
        "livability": 6, 
        "moons": 43, 
        "name": "New Pretend Planet Y",
    }

    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)
    actual_planet = Planet.query.get(1)

    #assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"
    assert actual_planet.color == EXPECTED_PLANET["color"]
    assert actual_planet.is_dwarf == EXPECTED_PLANET["is_dwarf"]
    assert actual_planet.livability == EXPECTED_PLANET["livability"]
    assert actual_planet.moons == EXPECTED_PLANET["moons"]
    assert actual_planet.name == EXPECTED_PLANET["name"]