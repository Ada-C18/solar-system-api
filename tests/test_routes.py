
def test_empty_database_returns_empty_list(client):

    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, one_saved_planet):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"name": "Earth", "description": "Blue planet", "rings": False, "id": 1}

def test_get_one_planet_when_empty_returns_error(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message" : "planet 1 not found"}

def test_get_planets_returns_200(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2

def test_create_planet_returns_201(client):
    response = client.post("/planets", json = {
        "name": "Mars",
        "description": "Angry red",
        "rings": False
    })
    response_body = response.get_data(as_text = True)

    assert response.status_code == 201
    assert response_body == "Planet Mars successfully created"
    