from bateau import Bateau

b1 = Bateau(1,3, longueur=3, vertical=True)
b2 = Bateau(3,5, longueur=2, vertical=False)
print(b1.position)
print(b2.position) 

b3= Bateau(5,0,3)
b4= Bateau(2,2,4,True)
print(b3.position)
print(b4.position)