from unittest.mock import patch

from pytemplate import main


def test_buy_ticket_for_children(capsys):
    inputs = ["Frozen", "8", "6"]
    with patch("builtins.input", side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert captured.out == "You are allowed to watch Frozen.\n"


def test_buy_ticket_for_teens(capsys):
    inputs = ["Batman", "16", "13"]
    with patch("builtins.input", side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert captured.out == "You are allowed to watch Batman.\n"


def test_age_limit(capsys):
    inputs = ["Blabla", "20", "10"]
    with patch("builtins.input", side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert captured.out == "We don't support this age limit.\n"


def test_children_not_allowed(capsys):
    inputs = ["Frozen", "5", "6"]
    with patch("builtins.input", side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert captured.out == "Sorry, you are not old enough to watch Frozen!\n"


def test_teens_not_allowed(capsys):
    inputs = ["Batman", "12", "13"]
    with patch("builtins.input", side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert captured.out == "Sorry, you are not old enough to watch Batman!\n"
