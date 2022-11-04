def test_get_one_planet(client):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "name" : "",
        "surface_area": "",
        "moons": "",
        "distance_from_sun": "",
        "namesake": ""      
        }
    