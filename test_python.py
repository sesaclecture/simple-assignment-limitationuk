import python

def test_name_type():
    assert isinstance(python.name, str)

def test_age_type():
    assert isinstance(python.age, int)

def test_numbers_content():
    assert 2 in python.numbers
    assert len(python.numbers) == 3

def test_is_student():
    assert python.is_student is True