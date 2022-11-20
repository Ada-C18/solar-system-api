from app.models.planet import Planet

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(
                    id = 1, 
                    color = "pink",    
                    is_dwarf = True, 
                    livability = 3, 
                    moons = 99,
                    name = "Pretend Planet X")
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] == 1
    assert result["color"] == "pink"
    assert result["livability"] == 3
    assert result["moons"] == 99
    assert result["name"] == "Pretend Planet X"
    
def test_to_dict_missing_id():
    # Arrange
    test_data = Planet( 
                color = "pink",    
                is_dwarf = True, 
                livability = 3, 
                moons = 99,
                name = "Pretend Planet X")
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] is None
    assert result["color"] == "pink"
    assert result["livability"] == 3
    assert result["moons"] == 99
    assert result["name"] == "Pretend Planet X"
    
        

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id = 1, 
                    color = "pink",    
                    is_dwarf = True, 
                    livability = 3, 
                    moons = 99)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] == 1
    assert result["color"] == "pink"
    assert result["livability"] == 3
    assert result["moons"] == 99
    assert result["name"] is None

def test_to_dict_missing_moons():
    # Arrange
    test_data = Planet(id = 1, 
                    color = "pink",    
                    is_dwarf = True, 
                    livability = 3, 
                    name = "Pretend Planet X")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 6
    assert result["id"] == 1
    assert result["color"] == "pink"
    assert result["livability"] == 3
    assert result["moons"] is None
    assert result["name"] == "Pretend Planet X"