import random
from bateau import Bateau

class Grille:
    def __init__(self, lignes, colonnes):
        self.vide = '~ '
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [ self.vide for i in range(self.lignes * self.colonnes)]

    def tirer(self, l, c, touche='x '):
        if self.grille[l*self.colonnes + c] != 'x ':
            self.grille[l*self.colonnes + c] = touche
            return True
        else:
            return False 
            
    def __str__(self):
        res = ''
        for i in range(self.lignes):
            for j in range(self.colonnes):
                res += self.grille[i*self.colonnes + j] 
            res += '\n'
        return res  
    
    def ajoute(self, b):
        for k in b.position:
            if k[0] < 0 or k[0] >= self.lignes or k[1] < 0 or k[1] >= self.colonnes:
                return False
        for k in b.position:
            if self.grille[k[0]*self.colonnes + k[1]] not in [self.vide, '💣']:
                return False
        for k in b.position:
            self.grille[k[0]*self.colonnes + k[1]] =  b.marque
        return True
    
    def placement_aleatoire(self, longueur):
        placements_possibles = []
        for i in range(self.lignes):
            for j in range(self.colonnes):
                b_h = Bateau(i, j, longueur=longueur, vertical=False)
                if self.ajoute(b_h):
                    placements_possibles.append([i, j, False])
                    for k in b_h.position:
                        self.grille[k[0]*self.colonnes + k[1]] =  self.vide
                b_v = Bateau(i, j, longueur=longueur, vertical=True)
                if self.ajoute(b_v):
                    placements_possibles.append([i, j, True])
                    for k in b_v.position:
                        self.grille[k[0]*self.colonnes + k[1]] =  self.vide
        l,c, vertical= random.choice(placements_possibles)
        self.ajoute(Bateau(l, c, longueur=longueur, vertical=vertical))
        return (l, c, vertical)
                

