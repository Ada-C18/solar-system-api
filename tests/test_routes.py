from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planet")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_returns_planet(client, one_saved_planet):
    response = client.get("/planet/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body["id"] == 1
    assert response_body["name"] == "Pluto"
    assert response_body["description"] == "cold and icy"
    assert response_body["distance"] == 15

def test_get_one_planet_missing_record(client):
    response = client.get("/planet/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 404
    assert response_body == {"message":"Planet 1 not found"}
   
def test_get_planets_with_all_records(client, two_saved_planets):
    response = client.get("/planet")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name":"Pluto", 
        "description":"cold and icy", 
        "distance":15
    }
    assert response_body[1] == {
        "id": 2,
        "name":"Venus", 
        "description":"round and far away", 
        "distance": 42
    }

def test_create_one_planet(client):
    response = client.post("/planet", json={
        "name":"Venus", 
        "description":"round and far away", 
        "distance": 42
    })
    response_body = response.get_data(as_text=True)

    # assert
    assert response.status_code == 201
    assert response_body == "Planet Venus successfully created"