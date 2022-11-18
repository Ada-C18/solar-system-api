from app.models.planet import Planet
# from app.tests.conftest import one_planet

def test_get_all_planets_returns_empty_list_when_db_empty(client):
    response = client.get("/planet")
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_one_planet_returns_seeded_planet(client, one_planet):
    response = client.get(f"/planet/{one_planet.id}")
    response_body = response.get_json()

    assert response.status_code==200
    assert response_body['id'] == one_planet.id
    assert response_body['name'] == one_planet.name
    assert response_body['color'] == one_planet.color
    assert response_body['description'] == one_planet.description

def test_create_planet_can_create_planet_in_empty_db(client):
    # arrange
    EXPECTED_PLANET = {
        "name": "Earth",
        "color": "green",
        "description": "dying"
    }
    # We can assume that ID is 1 because we started from an empty DB
    EXPECTED_ID = 1

    # act
    response = client.post("/planet", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    actual_planet = Planet.query.get(EXPECTED_ID)

    # assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} has been created"
    assert actual_planet.id == EXPECTED_ID
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.color == EXPECTED_PLANET["color"]
    assert actual_planet.description == EXPECTED_PLANET["description"]