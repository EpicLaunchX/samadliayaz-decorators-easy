from typing import Callable

from pytemplate.domain.models import Movie


def age_limit_6plus(func: Callable[[Movie], str]) -> Callable[[Movie], str]:
    def wrapper(movie: Movie):
        if movie.customer_age < 6:
            return f"Sorry, you are not old enough to watch {movie.name}!"
        return func(movie)

    return wrapper
