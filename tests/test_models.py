from app.models.planet import Planet

def test_to_dict_no_missing_data():
    test_data = Planet(id = 1,
                    name="Mercury",
                    description="distance_from_sun: 36.04 million mi",
                    num_moons=0)

    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "distance_from_sun: 36.04 million mi"
    assert result["num_moons"] == 0


def test_to_dict_missing_id():
    test_data = Planet(
                    name="Mercury",
                    description="distance_from_sun: 36.04 million mi",
                    num_moons=0)

    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mercury"
    assert result["description"] == "distance_from_sun: 36.04 million mi"
    assert result["num_moons"] == 0


def test_to_dict_missing_title():
    test_data = Planet(
                    id=1,
                    description="distance_from_sun: 36.04 million mi",
                    num_moons=0)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "distance_from_sun: 36.04 million mi"
    assert result["num_moons"] == 0


def test_to_dict_missing_description():
    test_data = Planet(id = 1,
                    name="Mercury",
                    num_moons=0)

    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] is None
    assert result["num_moons"] == 0


def test_to_dict_missing_num_moons():
    test_data = Planet(id = 1,
                    name="Mercury",
                    description="distance_from_sun: 36.04 million mi")

    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "distance_from_sun: 36.04 million mi"
    assert result["num_moons"] is None