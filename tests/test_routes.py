def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_records(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id":1,
        "name": "Jupiter",
        "description": "big planet",
        "moons": 80
    },
                             {
        "id":2,
        "name": "Mercury",
        "description": "small planet",
        "moons": 0
    }]

def test_get_planet_by_id(client, two_saved_planets):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name": "Jupiter",
        "description": "big planet",
        "moons": 80
    }

def test_get_planet_by_id_not_found(client, two_saved_planets):
    response = client.get("planets/6")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet 6 not found"}

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Neptune",
        "description": "named after the Roman god of the sea",
        "moons": 14
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Neptune successfully created"
