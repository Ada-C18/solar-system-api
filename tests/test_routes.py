# get all planets and return no records
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_missing_record(client, two_saved_planets):
    # Act
    response = client.get("/planets/5")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"planet 5 not found"}

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Big Planet",
        "description": "whatever",
        "size": "Big"
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "The Best!"
        "size": "medium"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet successfully created"


