from grille import Grille
from bateau import Bateau

g= Grille(5, 8)
print(g)
g.tirer(2,3)
print(g)

g.ajoute(Bateau(1,1,longueur=3, vertical=False))
print(g)