import mock
from Hangman1 import play


def test_play():
    with mock.patch('builtins.input', side_effect='east'):
        assert play() == 0
