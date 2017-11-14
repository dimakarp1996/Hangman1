
from Hangman1 import loss


def test_loss():
    assert loss(5, 7) == 'You won!'
    assert loss(7, 7) == 'You lost!'
    assert loss(9, 7) == 'You lost!'
