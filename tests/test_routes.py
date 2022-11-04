from app.routes import validate_model
from app.models.planet import Planet
from werkzeug.exceptions import HTTPException
import pytest



def test_read_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_read_one_planet(client, two_saved_planets):

    response = client.get("/planets/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 2,
        "name": "Earth",
        "description": "a little polluted",
        "color": "purple"
    }
def test_create_planet(client):
    # Arrange
    new_planet = {
        "name": "Colorful Planet",
        "description": "The Best!",
        "color": "rainbow"
    }
    # Act
    response = client.post("/planets", json=new_planet)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Colorful Planet successfully created"

def test_update_planet(client, two_saved_planets):
    # arrange
    updated_planet = {
        "name": "Zaelas Home",
        "color": "Cinnamon spice and everything nice",
        "description":"a baby planet"
    }
    #  act
    response = client.put("/planets/1", json=updated_planet)
    response_body = response.get_json()

    # assert
    assert response_body == "planet #1 successfully updated"
    assert response.status_code == 200

def test_update_planet_invalid_id(client, two_saved_planets):
    # arrange
    updated_planet = {
        "name": "Zaelas Home",
        "color": "Cinnamon spice and everything nice",
        "description":"a baby planet"
    }
    #  act
    response = client.put("/planets/lala", json=updated_planet)
    response_body = response.get_json()

    # assert
    assert response_body == {"message": "Planet lala invalid"}
    assert response.status_code == 400

def test_update_planet_extra_keys(client, two_saved_planets):
    # arrange
    updated_planet = {
        "name": "Zaelas Home",
        "color": "Cinnamon spice and everything nice",
        "description":"a baby planet"
    }
    #  act
    response = client.put("/planets/1", json=updated_planet)
    response_body = response.get_json()

    # assert
    assert response_body == "planet #1 successfully updated"
    assert response.status_code == 200
    
def test_update_planet_not_in_database(client, two_saved_planets):
    # arrange
    updated_planet = {
        "name": "Zaelas Home",
        "color": "Cinnamon spice and everything nice",
        "description":"a baby planet"
    }
    #  act
    response = client.put("/planets/3", json=updated_planet)
    response_body = response.get_json()

    # assert
    assert response_body == {"message":"Planet 3 not found"}
    assert response.status_code == 404
    
def test_delete_planet(client, two_saved_planets):
    response = client.delete("/planets/1")
    response_body = response.get_json()

    assert response_body == "planet #1 successfully deleted"
    assert response.status_code == 200

def test_delete_planet_not_in_database(client, two_saved_planets):
    
    #  act
    response = client.delete("/planets/3", json={
        "name": "Zaelas Home",
        "color": "Cinnamon spice and everything nice",
        "description":"a baby planet",
        "language": "baby talk"
    })
    response_body = response.get_json()

    # assert
    assert response_body == {"message":"Planet 3 not found"}
    assert response.status_code == 404
def test_delete_planet_invalid_id(client, two_saved_planets):
    #  act
    response = client.delete("/planets/lala")
    response_body = response.get_json()

    # assert
    assert response_body == {"message": "Planet lala invalid"}
    assert response.status_code == 400


def test_validate_model(two_saved_planets):
    result = validate_model(Planet,1)

    assert result.name == "Jupiter"
    assert result.id == 1
    assert result.description == "big"
    assert result.color == "pink"

def test_validate_model_invalid_id(two_saved_planets):

    
    with pytest.raises(HTTPException):
        result = validate_model(Planet,"lala")

def test_validate_model_missing_record(two_saved_planets):
    
    
    with pytest.raises(HTTPException):
        result = validate_model(Planet, 3)
