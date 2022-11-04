from app.models.planet import Planet

def create_mock_data(client):
    a = {
        "name": "foo1",
        "color": "bar1",
        "description": "foobar1"
    }

    b = {
        "name": "foo2",
        "color": "bar2",
        "description": "foobar2"
    }

    c = {
        "name": "foo3",
        "color": "bar3",
        "description": "foobar3"
    }

    client.post("/planets", json=a)
    client.post("/planets", json=b)
    client.post("/planets", json=c)

def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    #act
    response = client.get("/planets")

    #assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_all_planets(client, three_planets):
    #act
    # create_mock_data(client)
    response = client.get("/planets")
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body[0]["name"] == "foo1"
    assert response_body[1]["name"] == "foo2"
    assert response_body[2]["name"] == "foo3"
    assert response_body[0]["color"] == "bar1"
    assert response_body[1]["color"] == "bar2"
    assert response_body[2]["color"] == "bar3"
    assert response_body[0]["description"] == "foobar1"
    assert response_body[1]["description"] == "foobar2"
    assert response_body[2]["description"] == "foobar3"

def test_get_one_planet_returns_seeded_planet(client, one_planet):
    #act
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["color"] == one_planet.color
    assert response_body["description"] == one_planet.description


def test_get_one_planet_returns_not_found_planet(client, one_planet):
    #act
    response = client.get(f"/planets/10")
    response_body = response.get_json()

    #assert
    assert response.status_code == 404



def test_create_planet_can_create_planet_in_empty_db(client):
    # arrange
    EXPECTED_PLANET = {
        "name": "Neptune",
        "color": "blue",
        "description": "Dark, cold, and whipped by supersonic winds, ice giant Neptune is the eighth and most distant planet in our solar system"
    }

    EXPECTED_ID = 1

    # act
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)


    actual_planet = Planet.query.get(EXPECTED_ID)

    # assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} has been created"
    assert actual_planet.id == EXPECTED_ID
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.color == EXPECTED_PLANET["color"]
    assert actual_planet.description == EXPECTED_PLANET["description"]
