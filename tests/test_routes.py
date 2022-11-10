def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, one_planet_in_database):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "Tiny. Close to the Sun."
    }



def test_404_no_planet_id_1(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": f"Planet 1 not found"}, 404


def test_400_invalid_planet_id_1(client):
    # Act
    response = client.get("/planets/one")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": f"Planet one invalid"}, 400



def test_get_all_planets(client, one_planet_in_database):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1


def test_create_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "Our watery home planet."
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Earth has been added to the Planets database."


def test_update_planet_entry(client, one_planet_in_database):
    # Act
    response = client.put("/planets/1", json={
        "name": "Earth",
        "description": "Our watery home planet is also green."
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Earth has been updated in the Planets database."


def test_delete_planet_entry(client, one_planet_in_database):
    # Act
    response = client.delete("/planets/1", json={
        "name": "Earth",
        "description": "Our watery home planet is also green."
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet Mercury has been deleted from the Planets database."