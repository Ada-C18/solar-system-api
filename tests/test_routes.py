from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200 
    assert response_body == []

def test_get_one_planet_returns_planet(client, one_saved_planet):
    # act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # assert 
    assert response.status_code == 200 
    assert response_body["id"] == one_saved_planet.id
    assert response_body["name"] == one_saved_planet.name
    assert response_body["size"] == one_saved_planet.size
    assert response_body["description"] == one_saved_planet.description

def test_get_one_nonexistant_planet_returns_error_message(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404 
    assert response_body["message"] == "Planet 1 not found"

def test_create_planet_happy_path(client):
    # arrange
    EXPECTED_PLANET = {
        'name':'Earth',
        'size':4, 
        'description':'nice'
    }

    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)
    actual_planet = Planet.query.get(1)

    # assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} was successfully created"
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.size == EXPECTED_PLANET["size"]
    assert actual_planet.description == EXPECTED_PLANET["description"]