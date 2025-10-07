from bateau import Bateau

def test_bateau_defaults():
    b = Bateau(2, 3)
    assert b.longueur == 1
    assert b.vertical == False
