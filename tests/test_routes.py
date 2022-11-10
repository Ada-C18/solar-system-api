def test_get_all_planets_with_no_records(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, one_saved_planet):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    assert response_body["id"] == one_saved_planet.id
    assert response_body["name"] == one_saved_planet.name
    assert response_body["description"] == one_saved_planet.description
    assert response_body["moons"] == one_saved_planet.moons

def test_get_one_planet_no_data(client):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 1 not found"}

def test_get_planets_happy_path(client, one_saved_planet):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    assert response_body[0] == {"id": 1, "name": "Earth", "description": "home", "moons": 1}

def test_create_planet_happy_path(client):
    #Arrange
    test_planet = {"name": "Mars", "description": "red", "moons": 0}
    #Act
    response = client.post("/planets", json={"name": "Mars", "description": "red", "moons": 0})
    response_body = response.get_data(as_text=True)
    #Assert
    assert response.status_code == 201
    assert response_body == "Planet Mars successfully created"
