def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Giant 2",
        "description": "Even bigger than the first!",
        "moon_count": 130
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Neptune",
        "description": "it may exist, it may not",
        "moon_count": 0
    }

def test_get_all_planets_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_moon_count_query_matching_one(client, two_saved_planets):
    data = {'moon_count': 0}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 2,
        "name": "Neptune",
        "description": "it may exist, it may not",
        "moon_count": 0
    }

def test_get_all_planets_with_moon_count_query_matching_none(client, two_saved_planets):
    data = {'moon_count': 671}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_planet_by_id(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Giant 2",
        "description": "Even bigger than the first!",
        "moon_count": 130
    }

def test_get_planet_by_id_no_records(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message":"Planet 1 not found"}

def test_get_planet_by_invalid_id(client, two_saved_planets):
    response = client.get("/planets/cat")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message":"Planet cat invalid"}

def test_create_planet(client):
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "That's us!",
        "moon_count": 1
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"