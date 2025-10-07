from bateau import Bateau
from grille import Grille

class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical= vertical, marque="🚢")