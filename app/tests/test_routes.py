
"""
TODO: 
- create a new planet ***DONE***
- (GET, 200) one planet w/ ID ***DONE***
- (GET, 200) all planet(s)
- update planet (POST, 200) 
- delete planet (DELETE, 200) ***DONE***
- validate planet (GET,200 - id) ***DONE***
"""

#INPROGRESS
# def test_get_all_planets_return_no_records(client):
#     #pass
#     #act
#     response = client.get('/planets')
#     response_body = response.get_json()

#     #assert
#     assert response.status_code == 200
#     assert response_body == []

#INPROGRESS
# def test_get_all_planets(client, saved_test_planets):
#     # pass
#     #act
#     response = client.get('/planets')
#     # response_body = response.get_json()
#     response_body = response.get_data(as_text=True)

#     #assert
#     assert response.status_code == 200
#     assert response_body == [{
#         'id': 1,
#         'color': 'pink',
#         'is_dwarf': True, 
#         'livability': 3, 
#         'moons': 99, 
#         'name': 'Pretend Planet X'
#         # "id": 1,
#         # "color": "pink",
#         # "is_dwarf": True, 
#         # "livability": 3, 
#         # "moons": 99, 
#         # "name": "Pretend Planet X"
#         },
#         {
#         "id": 2,
#         "color": "purple",
#         "is_dwarf": False, 
#         "livability": 7.4,
#         "moons": 1,
#         "name": "Planet Pretend Z"
#         }]

def test_get_one_book_by_id(client, saved_test_planets):
    #pass
    #act
    response = client.get('/planets/1')
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body == {
        'id': 1,
        'color': "pink",
        'is_dwarf': True, 
        'livability': 3, 
        'moons': 99, 
        'name': "Pretend Planet X",
    }

def test_create_one_new_planet(client):
    #pass
    #act
    response = client.post("/planets", json={
        "color": "green",
        "is_dwarf": False, 
        "livability": 5.5, 
        "moons": 43, 
        "name": "New Pretend Planet Y",
    })
    # response_body = response.get_json()
    response_body = response.get_data(as_text=True)

    #assert
    assert response.status_code == 201
    assert response_body == "Planet New Pretend Planet Y successfully created"

