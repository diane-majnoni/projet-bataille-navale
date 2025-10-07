from bateau import Bateau
from grille import Grille

def test_defaults():
    b = Bateau(2, 3)
    assert b.longueur == 1
    assert not b.vertical

def test_position():
    b1 = Bateau(1, 1, longueur=3, vertical=False)
    assert b1.position == [(1, 1), (1, 2), (1, 3)]
    b2 = Bateau(0, 0, longueur=2, vertical=True)
    assert b2.position == [(0, 0), (1, 0)]

def test_coulé():
    g = Grille(8, 8)
    b = Bateau(1, 1, longueur=4, vertical=False)
    g.tirer(1, 1)
    g.tirer(1, 2)
    assert not b.coulé(g)
    g.tirer(1, 3)
    g.tirer(1, 4)
    assert b.coulé(g)

