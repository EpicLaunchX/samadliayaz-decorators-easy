from pytemplate.domain.models import movie_factory
from pytemplate.service.tickets import buy_ticket_for_children, buy_ticket_for_teens


def main():
    movie_name = input("Please, enter the name of the movie: ")
    customer_age = int(input("Please, enter the age of the customer: "))
    age_limit = int(input("Please, enter the age limitation: "))

    if age_limit == 6:
        print(buy_ticket_for_children(movie_factory(movie_name, customer_age)))
    elif age_limit == 13:
        print(buy_ticket_for_teens(movie_factory(movie_name, customer_age)))
    else:
        print("We don't support this age limit.")
