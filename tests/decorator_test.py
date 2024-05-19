from pytemplate import buy_ticket_for_children, buy_ticket_for_teens, Movie


def test_decorator():
    user1 = Movie("Breaking Bad", 5)
    user2 = Movie("Breaking Bad", 7)
    assert buy_ticket_for_children(user1) == f"Sorry, you are not old enough to watch {user1.name}!"
    assert buy_ticket_for_children(user2) == f"You are allowed to watch {user2.name}."


def test_buy_ticket_for_teens():
    user3 = Movie("Breaking Bad", 10)
    user4 = Movie("Breaking Bad", 14)
    assert buy_ticket_for_teens(user3) == f"Sorry, you are not old enough to watch {user3.name}!"
    assert buy_ticket_for_teens(user4) == f"You are allowed to watch {user4.name}."
