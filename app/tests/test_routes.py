from app.models.planet import Planet


def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
    
def test_get_one_planet(client,one_planet):
    # Act
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] ==one_planet.description
    assert response_body["diameter"]==one_planet.diameter
    
def test_create_planet_can_create_planet_in_empty_db(client):   
    EXPECTED_PLANET={ "name": "Mercury",
                    "description": "watr 4evr", "diameter":39999}
    EXPECTED_ID =1

    # Act
    
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)
    
    actual_planet = Planet.query.get(EXPECTED_ID)

    # assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} has been created"
    assert actual_planet.id == EXPECTED_ID
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.description == EXPECTED_PLANET["description"]
    assert actual_planet.diameter == EXPECTED_PLANET["diameter"]
    
def test_no_data_in_test_database(client):
    #Act
    response=client.get("/planets/1") 
    response_body=response.get_json() 
    #Assert 
    assert response.status_code==404 
