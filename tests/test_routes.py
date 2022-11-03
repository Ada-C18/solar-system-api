from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, one_saved_planet):
    response = client.get("/planets/1")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Kangaroo Planet",
        "description": "Australia wasn't big enough for them",
        "color": "Brown and Gray"
    }

def test_planets_with_no_data(client):
    response = client.get("/planets/1")
    response_body = response.get_json()
    
    assert response.status_code == 404

def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Cat Planet",
        "description": "Funny",
        "color": "Gray"
    },
    {
        "id": 2,
        "name": "Dog Planet",
        "description": "Big",
        "color": "Brown"
    }]

def test_create_one_planet(client):
    response = client.post("/planets", json = {
        "name": "Giraffe Planet",
        "description": "No short necks here",
        "color": "Yellow and Brown"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Giraffe Planet successfully created"