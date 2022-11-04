def test_get_all_planets_with_no_records(client):
    # act
    response = client.get("/solar-system")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_returns_planet(client, one_saved_planet):
    # act
    response = client.get("solar-system/1")
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body["id"] == one_saved_planet.id
    assert response_body["name"] == one_saved_planet.name
    assert response_body["distance_from_sun"] == one_saved_planet.distance_from_sun
    assert response_body["description"] == one_saved_planet.description