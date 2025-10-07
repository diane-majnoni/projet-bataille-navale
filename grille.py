class Grille:
    def __init__(self, lignes, colonnes):
        self.vide = '~'
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [ self.vide for i in range(self.lignes * self.colonnes)]

    def tirer(self, l, c):
        if self.grille[l*self.colonnes + c] == self.vide:
            self.grille[(l-1)*self.colonnes + (c-1)] = 'x'
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