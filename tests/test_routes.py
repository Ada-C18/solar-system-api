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