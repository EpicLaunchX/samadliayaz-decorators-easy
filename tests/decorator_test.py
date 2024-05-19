from pytemplate import buy_ticket_for_children, Movie


def test_decorator():
    user1 = Movie("Breaking Bad", 5)
    user2 = Movie("Breaking Bad", 7)
    assert buy_ticket_for_children(user1) == \
        f"Sorry, you are not old enough to watch {user1.name}!"
    assert buy_ticket_for_children(user2) == \
        f"You are allowed to watch {user2.name}."
