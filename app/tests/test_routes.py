from app.models.planet import Planet

def test_get_all_planets_with_empty_db_return_empty_list(client):

    response = client.get('/planets')
    response_body = response.get_json()

    assert response_body == []
    assert response.status_code == 200

def test_get_one_planet(client,two_saved_planets):

    response = client.get('/planets/2')
    response_body = response.get_json()

    planet2 = {
        'id':2,
        'name': 'Blorp',
        'color': 'Purple',
        'description': 'Stinky'
    }

    # florpus ={
    #             "id": 3,
    #             "name": 'Florpus',
    #             "color": 'Red',
    #             "description": "Shy"
    #         }

    assert response.status_code == 200
    assert response_body == planet2
