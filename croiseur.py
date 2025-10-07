from bateau import Bateau
from grille import Grille

class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical= vertical, marque = "⛴")