class Grille:
    def __init__(self, lignes, colonnes):
        self.vide = '~ '
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [ self.vide for i in range(self.lignes * self.colonnes)]

    def tirer(self, l, c):
        if self.grille[l*self.colonnes + c] == self.vide:
            self.grille[l*self.colonnes + c] = 'x '
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
            if self.grille[k[0]*self.colonnes + k[1]] != self.vide:
                return False
        for k in b.position:
            self.grille[k[0]*self.colonnes + k[1]] = '⛵'
        return True