from grille import Grille

class Bateau:
    def __init__(self, ligne, colonne,longueur=1, vertical=False):
      self.ligne = ligne
      self.colonne = colonne
      self.longueur = longueur
      self.vertical = vertical

    @property
    def position(self):
        if self.vertical:
            return [(self.ligne +i, self.colonne) for i in range(self.longueur)]
        else:
            return [(self.ligne, self.colonne +i) for i in range(self.longueur)]
        
    
    def coulé(self,grille):
        for k in self.position:
            if grille.grille[k[0]*grille.colonnes + k[1]] != 'x':
                return False
        return True