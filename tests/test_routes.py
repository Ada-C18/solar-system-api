from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planet")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []