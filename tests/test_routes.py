from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    response = client.get('/planets')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet_returns_four_items(client, two_saved_planets):
    response = client.get('/planets/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "description": "good vibes",
        "id": 1,
        "name": "Earth",
        "radius": 6371
    }

def test_get_one_planet_returns_404(client):
    response = client.get('/planets/1')
    response_body = response.get_json()

    assert response.status_code == 404



def test_get_all_planets_returns_two_dictionaries(client, two_saved_planets):
    response = client.get('/planets')
    response_body = response.get_json()
    planets = Planet.query.all()
    planet_response = [planet.to_dict() for planet in planets]

    assert response.status_code == 200
    assert response_body == planet_response

def test_create_planet_record_returns_201(client, two_saved_planets):
    response = client.post('/planets', json={
        'name': 'Mercury',
        'radius':  2439.7,
        'description': 'amazing place'
    })
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == 'Planet: Mercury succesfully created'