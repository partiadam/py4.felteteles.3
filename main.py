'''
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
'''

from random import randint

szam = randint(0,5)
beker = int(input('Adj meg egy számot: \t'))
if beker == szam:
    print('Eltaláltad!')
        
if beker > szam:
    print('Nagyobb az általad gondolt szám.')
if beker < szam:
    print('Kisebb az általad gondolt szám.')