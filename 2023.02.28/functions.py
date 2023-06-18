from data import *

def readFile():
    f = open("pilotak.csv", "r", encoding="UTF-8")
    f.readline()
    for sor in f:
        pilotak.append(Pilota(sor))
    f.close()

def szazad():
    for item in pilotak:
        if int(item.szul[0:4]) < 1901:
            print(f"\t{item.nev} ({item.szul})")
        
def nemzetiseg():
    minpoz=0
    for i in range(len(pilotak)):
        if pilotak[i].rajtszam != "" and pilotak[i].rajtszam < pilotak[minpoz].rajtszam:
            minpoz = i
    return pilotak[minpoz].nemzetiseg

rajtszamok={}
for vers in pilotak:
    if vers.rajtszam !="":
        if vers.rajtszam in rajtszamok.keys():
            rajtszamok[vers.rajtszam] += 1
        else:
            rajtszamok[vers.rajtszam] = 1

print("7. feladat: ", end = "")
db=0
for key, value in rajtszamok.items():
    if value > 1:
        if db == 0:
            print(f"{key}", end="")
        else:
            print(f", {key}", end="")    
        db+=1
        print(f"{key}", end="")