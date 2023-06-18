import random

szamok=[]

def feltolt():
    for i in range(15):
        szamok.append(random.randint(0, 100))

def kiir():
    for item in szamok:
        print(item, end=" ")


#---------------------------------------------

# összegzés: mennyi a listában lévő számok összege
def osszeg():
    osszeg=0
    for item in szamok:
        osszeg+=item
    return osszeg 

#megszámlálás:
def paratlanDb():
    darab=0
    for item in szamok:
        if item %2 == 1:
            darab+=1
    return darab

#eldöntés: benne van-e a számok között a paraméterben kapott szám
def eldontes(szam):
    for item in szamok:
        if item == szam:
            return True
    return False

def eldontes_klasszikus(szam):
    i = 0
    while i < len(szamok) and szamok[i] != szam:
        i+=1
        #ha az i = elemszámmal akkor nincs benne
        #ha az i < elemszám, megtaláltuk az elemet és az i megállt ahol megtaláltuk
    if i==len(szamok):
        return False
    else:
        return True

#keresés: a keresett érték első előfordulásának pozícióját adja vissza
def kereses(keresett):
    for index,ertek in enumerate(szamok):
        if keresett == ertek:
            return index
    return -1

#szélsőérték (maximum) kiválasztása

#--------------------------------------------
feltolt()
kiir()
print(f"\nA számok összege: {osszeg()}")
print(f"\n a páratlan számok száma: {paratlanDb()}")
print(f"A páros számok darabszáma: {len(szamok) - paratlanDb()}")

szam = int(input("Mit keresek"))
if eldontes(szam):
    print("a keresett szám benne van a listában")
    print(f"A keresett szám {kereses(szam) + 1}. a listában.")
else:
    print("a kersett szám nincs a listában")
print(max(szamok))