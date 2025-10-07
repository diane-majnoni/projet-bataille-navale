from bateau import Bateau
from grille import Grille   

class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical= vertical, marque="🐟")