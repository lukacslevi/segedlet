from data import *
from typing import List

nobelDijasok=[]
nobelDijasok:List[NobelDijas]=[]

#2. feladat
file=open("nobel.csv", "r", encoding="UTF-8")
file.readline()
for sor in file:
    nobelDijasok.append(NobelDijas(sor))

#3.feladat
for item in nobelDijasok:
    if item.keresztnev == "Arthur B." and item.vezeteknev=="McDonald":
        print(f"3. feladat: {item.tipus}")

for item in nobelDijasok:
    if item.evszam == 2017 and item.tipus=="irodalmi":
        print(f"4. feladat: {item.keresztnev}")

#5.feladat
for item in nobelDijasok:
    if item.evszam >= 1990 and item.tipus=="béke" and item.vezeteknev=="":
        print(f"\t5. feladat: {item.evszam}")

for item in nobelDijasok:
    if "Curie" in item.vezeteknev:
        print(f"\t{item.evszam}: {item.keresztnev} {item.vezeteknev} {item.tipus}")