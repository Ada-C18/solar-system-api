from werkzeug.exceptions import HTTPException
from app.routes import validate_id
from app.models.planet import Planet
import pytest


# 1. `POST` `/planets` with a JSON request body returns a `201`

def test_get_planet_by_id(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "moons": 0,
        "description": "no watr 4evr"
    }

def test_get_planet_by_id_empty(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404


def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

    
def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()
    assert response_body[0] == {
        "id": 1,
        "name": "Mars",
        "moons": 0,
        "description": "no watr 4evr"
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Jupiter",
        "moons": 1,
        "description": "i luv storms"
    }

def test_get_query_param_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets?moons=0")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body[0] == {
        "id": 1,
        "name": "Mars",
        "moons": 0,
        "description": "no watr 4evr"
    }



def test_post_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "The Best!",
        "moons": 1
    })

    # Assert
    assert response.status_code == 201

def test_update_planet(client, two_saved_planets):
    # Act
    response = client.put("/planets/1", json = {
        "name":"Mars2",
        "description": "The Best!",
        "moons": 1
    })
    assert response.status_code == 200

def test_delete_planet(client, two_saved_planets):
    # Act
    response = client.delete("/planets/1")
    assert response.status_code == 200

def test_delete_planet_invalid_id(client, two_saved_planets):
    # Act
    response = client.delete("/planets/random")
    assert response.status_code == 400
