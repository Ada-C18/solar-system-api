def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

#1. GET /books/1 returns a response body that matches our fixture
def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()
    #response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 200
    assert response_body == {
        'id': 1,
        'name': 'Mars',
        'description': 'Too hot',
        'moons': 2
    }

#2. GET /books/1 with no data in test database (no fixture) returns a 404
def test_get_one_planet_not_in_db(client):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()
    #response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"Planet 3 not found"}

#3. GET /books with valid test data (fixtures) returns a 200 with an array including appropriate test data
def test_get_all_planets_with_two_planets_db(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
            'id': 1,
            'name': 'Mars',
            'description': 'Too hot',
            'moons': 2}
        
    assert response_body[1] == {
            'id': 2,
            'name' : 'Earth',
            'description' : 'Home Sweet Home', 
            'moons': 1}


# 4.POST /books with a JSON request body returns a 201
def test_create_one_book(client):
    # Act
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "Beautiful planet!",
        "moons": 3
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet New Planet successfully created"
