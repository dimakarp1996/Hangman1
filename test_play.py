import mock
from Hangman import play


def test_play():
    with mock.patch('builtins.input', side_effect='east'):
        assert play() == 0
