from app.models.planet import Planet


def test_get_all_planets_with_empty_db_return_empty_list(client):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response_body == []
    assert response.status_code == 200


def test_get_all_planets(client, two_saved_planets):
    response = client.get('/planets')
    response_body = response.get_json()

    mercury = {
        "id": 1,
        "name": "Mercury",
        "description": "distance_from_sun: 36.04 million mi",
        "number of moons": 0
    }

    venus = {
        "id": 2,
        "name": "Venus",
        "description": "distance_from_sun: 67.24 million mi",
        "number of moons": 0
    }

    assert response_body == [mercury, venus]
    assert response.status_code == 200


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/2")
    response_body = response.get_json()

    venus = {
        "id": 2,
        "name": "Venus",
        "description": "distance_from_sun: 67.24 million mi",
        "number of moons": 0
    }

    # Assert
    assert response.status_code == 200

    assert response_body == venus


def test_get_one_planet_not_in_db(client):
    response = client.get('/planets/3')
    response_body = response.get_json()

    assert response_body == {"message": f"planet 3 not found"}
    assert response.status_code == 404


def test_post_planet_returns_201(client):
    response = client.post("/planets", json=
                            {"name": "Pluto",
                            "description": "distance_from_sun: 3.70 billion mi",
                            "num_moons": 5})
                            
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == 'Planet Pluto successfully created'

    new_planet = Planet.query.get(1)
    assert new_planet
    assert new_planet.name == "Pluto"
    assert new_planet.description == "distance_from_sun: 3.70 billion mi"
    assert new_planet.num_moons == 5


def test_get_all_planets_with_two_records(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Mercury",
        "description": "distance_from_sun: 36.04 million mi",
        "number of moons": 0
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Venus",
        "description": "distance_from_sun: 67.24 million mi",
        "number of moons": 0
    }


def test_get_all_planets_with_name_query_matching_none(client, two_saved_planets):
    data = {'name': 'Anything'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_all_planets_with_name_query_matching_one(client, two_saved_planets):
    data = {'name': 'Mercury'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "name": "Mercury",
        "description": "distance_from_sun: 36.04 million mi",
        "number of moons": 0
    }


def test_get_one_planet_id_not_found(client, two_saved_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"planet 3 not found"}


def test_get_one_planet_id_invalid(client, two_saved_planets):
    response = client.get("/planets/monkey")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message":"planet monkey invalid"}
