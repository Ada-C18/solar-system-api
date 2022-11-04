from werkzeug.exceptions import HTTPException
from app.routes import validate_model
from models.planet import Planet
import pytest

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

def test_get_all_planets_with_name_query_matching_one(client, two_saved_planets):
    data = {'name': "Neptune"}
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

def test_get_all_planets_with_name_query_matching_none(client, two_saved_planets):
    data = {'name': "This is such a fake name"}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()    

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

def test_update_planet(client, two_saved_planets):
    test_data = {
        "name": "Test",
        "description": "This is a test description",
        "moon_count": 42
    }

    response = client.put("/planets/1", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet #1 successfully updated"    

def test_delete_planet(client, two_saved_planets):
    response = client.delete("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet #1 successfully deleted"

def test_validate_model(two_saved_planets):
    result_planet = validate_model(Planet, 1)
    
    assert result_planet.id == 1
    assert result_planet.name == "Giant 2"
    assert result_planet.description == "Even bigger than the first!"
    assert result_planet.moon_count == 130

def test_validate_model_missing_record(two_saved_planets):
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "6")

def test_validate_model_invalid_id(two_saved_planets):
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "cat")