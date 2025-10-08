from grille import Grille
from bateau import Bateau
from torpilleur import Torpilleur
from croiseur import Croiseur
from porte_avion import PorteAvion
from sous_marin import SousMarin

grille_cachée = Grille(8,10)

placement_torpilleur = grille_cachée.placement_aleatoire(2)
torpilleur=Torpilleur(placement_torpilleur[0], placement_torpilleur[1], vertical=placement_torpilleur[2])

placement_sous_marin = grille_cachée.placement_aleatoire(2)
sousMarin=SousMarin(placement_sous_marin[0], placement_sous_marin[1], vertical=placement_sous_marin[2])

placement_croiseur = grille_cachée.placement_aleatoire(3)
croiseur=Croiseur(placement_croiseur[0], placement_croiseur[1], vertical=placement_croiseur[2])

placement_porte_avion = grille_cachée.placement_aleatoire(4)
porteAvion=PorteAvion(placement_porte_avion[0], placement_porte_avion[1], vertical=placement_porte_avion[2])

placement_bateaux = []
placement_bateaux += list(torpilleur.position)
placement_bateaux += list(sousMarin.position)
placement_bateaux += list(croiseur.position)
placement_bateaux += list(porteAvion.position)


print(grille_cachée)
grille = Grille(8,10)

positions_touchees = []
flotte = {'torpilleur':2, 'sous-marin':2, 'croiseur':3, 'porte-avion':4}
bateaux_coulés = 0
coups = 0
while bateaux_coulés < 4:
    print(grille)
    l = int(input("ligne visée :"))
    c = int(input("colonne visée :"))
    if l < 0 or l >= grille.lignes or c < 0 or c >= grille.colonnes:
        print("choisissez une position valide")
        continue
        
    if (l,c) in positions_touchees:
        print("cette posistion a déja été visée")
        continue
        
    if grille_cachée.grille[l*grille_cachée.colonnes + c] == grille_cachée.vide:
        print( "Dans l'eau !")
        coups += 1
        positions_touchees.append((l,c))
        grille.tirer(l,c)

    if (l,c) in placement_bateaux:
        coups += 1
        positions_touchees.append((l,c))
        if (l,c) in porteAvion.position:
            flotte['porte-avion'] -= 1
            if flotte['porte-avion'] == 0:
                print("Coulé !")
                bateaux_coulés += 1
                grille.ajoute(porteAvion)
            else:
                print("Touché !")
                grille.tirer(l,c,touche='💣')

        if (l,c) in croiseur.position:
            flotte['croiseur'] -= 1
            if flotte['croiseur'] == 0:
                print("Coulé !")
                bateaux_coulés += 1
                grille.ajoute(croiseur)
            else:
                print("Touché !")
                grille.tirer(l,c,touche ='💣')

        if (l,c) in sousMarin.position:
            flotte['sous-marin'] -= 1
            if flotte['sous-marin'] == 0:
                print("Coulé !")
                bateaux_coulés += 1
                grille.ajoute(sousMarin)
            else:
                print("Touché !")
                grille.tirer(l,c, touche ='💣')
        
        if (l,c) in torpilleur.position:
            flotte['torpilleur'] -= 1
            if flotte['torpilleur'] == 0:
                print("Coulé !")
                bateaux_coulés += 1
                grille.ajoute(torpilleur)
            else:
                print("Touché !")
                grille.tirer(l,c, touche ='💣')
        
print("Vous avez coulé tous les bateaux en", coups, "coups !")