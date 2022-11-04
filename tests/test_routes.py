
def test_get_all_planets_with_no_record(client):
        #act
        response = client.get("/planets")
        response_body = response.get_json()

        #assert
        assert response.status_code == 200
        assert response_body == []


def test_get_planet_by_id(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json=()
    
    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Giant 2",
        "description": "Even bigger than the first!",
        "moon_count": "130" 
    }
