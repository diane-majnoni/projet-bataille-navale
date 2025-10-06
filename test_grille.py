from grille import Grille

def test__init():
    g = Grille(5, 8)
    assert g.lignes == 5
    assert g.colonnes == 8
    assert g.grille == [g.vide] * 40

def test_tirer():
    g = Grille(5, 8)
    assert g.tirer(2, 3) == True
    assert g.tirer(2, 3) == False
