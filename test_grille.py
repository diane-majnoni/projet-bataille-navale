from grille import Grille
from bateau import Bateau

def test__init():
    g = Grille(5, 8)
    assert g.lignes == 5
    assert g.colonnes == 8
    assert g.grille == [g.vide] * 40

def test_tirer():
    g = Grille(5, 8)
    assert g.tirer(2, 3) == True
    assert g.tirer(2, 3) == False

def test_ajoute():
    g = Grille(6, 6)
    b1 = Bateau(1, 2, longueur=3, vertical=False)
    assert g.ajoute(b1) == True
    b2 = Bateau(3, 0, longueur=2, vertical=True)
    assert g.ajoute(b2) == True
    b3 = Bateau(1, 2, longueur=2, vertical=True)
    assert g.ajoute(b3) == False 
    b4 = Bateau(4, 4, longueur=3, vertical=False)
    assert g.ajoute(b4) == False  
    