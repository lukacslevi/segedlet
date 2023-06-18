szam=int(input("Kérek egy számot 5 és 30 között! "))
szamok=[]

def atlag():
    osszesszam=0
    eredmeny=0
    for item in szamok:
        osszesszam+=item
    eredmeny = osszesszam / len(szamok)
    return eredmeny

import random

if 5<=szam and 30>=szam:
    for i in range(szam):
        szamok.append(random.randint(0, 100))
    szamok.sort()
    print(szamok, end=' ')
    print(f"\na számok átlaga: {atlag()}")
else:
    print("hibás adat!")

