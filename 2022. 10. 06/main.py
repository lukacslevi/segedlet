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

def legnagyobb():
    max=szamok[0]
    maxIndex=0
    for i in range(1, len(szamok)):
        if szamok[i]>max:
            max=szamok[i]
            maxIndex=i
    return maxIndex

def legnagyobb2():
    maxIndex=0
    for i in range(1, len(szamok)):
        if szamok[i]>szamok[maxIndex]:
            maxIndex=i
    return maxIndex

def legnagyobb3():
    maxIndex=0
    for index, ertek in enumerate(szamok):
        if ertek>szamok[maxIndex]:
            maxIndex = index
    return maxIndex


#minimum kiválasztás

def legkisebb():
    min=szamok[0]
    minIndex=0
    for i in range(1, len(szamok)):
        if szamok[i]<min:
            min=szamok[i]
            minIndex=i
    return minIndex

#--------------------------------------------
feltolt()
kiir()
print(f"\nA számok összege: {osszeg()}")
print(f"\n a páratlan számok száma: {paratlanDb()}")
print(f"A páros számok darabszáma: {len(szamok) - paratlanDb()}")

print(f"A legnagyobb elem sorszáma: {legnagyobb()+1}. Értéke: {szamok[legnagyobb()]}")
print(f"A legkisebb elem sorszáma: {legkisebb()+1}. Értéke: {szamok[legkisebb()]}")