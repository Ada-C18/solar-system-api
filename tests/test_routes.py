from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # act
    response = client.get("/solar-system")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_returns_planet(client, one_saved_planet):
    # act
    response = client.get("/solar-system/1")
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body["id"] == one_saved_planet.id
    assert response_body["name"] == one_saved_planet.name
    assert response_body["distance_from_sun"] == one_saved_planet.distance_from_sun
    assert response_body["description"] == one_saved_planet.description

def test_get_one_planet_returns_404(client):
    # act
    response = client.get("/solar-system/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 404
    assert response_body == {'message': 'Planet 1 not found'}

def test_create_planet_happy_path(client):
    # arrange
    EXPECTED_PLANET = {
        "name": "Earth",
        "distance_from_sun": 93000000,
        "description": "only planet known to harbor intelligent life"
    }

    # act
    response = client.post("/solar-system", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)
    actual_planet = Planet.query.get(1)

    # assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.distance_from_sun == EXPECTED_PLANET["distance_from_sun"]
    assert actual_planet.description == EXPECTED_PLANET["description"]

# could include: 
# query test, 
# update_planet test, 
# delete_planet test, 
# and verify_model returning 400