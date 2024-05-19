from src.pytemplate import Movie


def test_value():
    obj = Movie("Breaking Bad", 50)
    assert obj.name == "Breaking Bad"
    assert obj.customer_age == 50


def test_type():
    obj = Movie("Breaking Bad", 2008)
    assert isinstance(obj.name, str)
    assert isinstance(obj.customer_age, int)
