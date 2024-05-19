from src.pytemplate import Movie, movie_factory


def test_value():
    obj = Movie("Breaking Bad", 50)
    assert obj.name == "Breaking Bad"
    assert obj.customer_age == 50


def test_type():
    obj = Movie("Breaking Bad", 50)
    assert isinstance(obj.name, str)
    assert isinstance(obj.customer_age, int)


def test_movie_factory():
    x = movie_factory("Breaking Bad", 50)
    assert isinstance(x, Movie)
    assert x.name == "Breaking Bad"
    assert x.customer_age == 50
