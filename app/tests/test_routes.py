def test_get_all_planets_with_no_records(client):
    response = client.get("/planets/")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == []


def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets/")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Venus",
            "description": "Hot mama",
            "mass": "The bigger the better.",
        },
        {
            "id": 2,
            "name": "Earth",
            "description": "There are bugs here",
            "mass": "normal",
        },
    ]


def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Venus",
        "description": "Hot mama",
        "mass": "The bigger the better.",
    }


def test_get_one_planet_no_data_returns_404(client):
    response = client.get("/planets/3")
    assert response.status_code == 404


def test_post_planet_returns_201(client):
    response = client.post("/planets/", json={
        "name": "Earth II",
        "description": "If Earth is so good why isn't there... oh",
        "mass": "Better than normal"
    })
    response_body = response.get_json()
    assert response.status_code == 201
    assert response_body == {"success": "Planet Earth II is now in orbit"}


def test_invalid_planet_id_returns_400(client):
    response = client.get("/planets/invalid")
    assert response.status_code == 400


def test_delete_planet(client, two_saved_planets):
    response = client.delete("/planets/1")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == {"success": "Planet #1 successfully deleted"}


def test_update_planet(client, two_saved_planets):
    response = client.put("/planets/1", json={
        "name": "Mercury",
        "description": "Actually, Planet 1 is totally mercury. What are you doing here Venus",
        "mass": "Correct"
    })
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == {"success": "Planet #1 successfully updated"}


def test_name_query(client, two_saved_planets):
    response = client.get("/planets/?name=Venus")
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Venus",
        "description": "Hot mama",
        "mass": "The bigger the better.",
    }]
