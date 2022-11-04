from app.models.planet import Planet

def test_get_all_planets_in_database(client, saved_test_planets):
    # Act
    response = client.get('/planets')
    response_body = Planet.query.all()

    # Assert
    assert response.status_code == 200

def test_missing_planet_id(client):
    # Act
    response = client.get('planets/3')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404

def test_get_planets_for_empty_database(client):
    # Act
    response = client.get('/planets')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_by_id(client, saved_test_planets):
    # Act
    response = client.get('/planets/1')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {'id': 1, 'color': "pink", 'is_dwarf': True, 'livability': 3, 'moons': 99, 'name': "Pretend Planet X"}

def test_create_one_new_planet(client):
    # Act
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

    # Assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"
    assert actual_planet.color == EXPECTED_PLANET["color"]
    assert actual_planet.is_dwarf == EXPECTED_PLANET["is_dwarf"]
    assert actual_planet.livability == EXPECTED_PLANET["livability"]
    assert actual_planet.moons == EXPECTED_PLANET["moons"]
    assert actual_planet.name == EXPECTED_PLANET["name"]