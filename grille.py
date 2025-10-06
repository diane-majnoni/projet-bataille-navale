class Grille:
    def __init__(self, lignes, colonnes):
        self.vide = '~'
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [ self.vide for i in range(self.lignes * self.colonnes)]

    def tirer(self, x, y):
        if self.grille[y*self.lignes + x] == self.vide:
            self.grille[y*self.lignes + x] = 'x'
            return True
        else:
            return False 