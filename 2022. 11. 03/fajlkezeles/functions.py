from genericpath import exists
from data import tanulok

fajl = "students.txt"

def menu():
    valasztott = ""
    print("--------------MENÜ--------------")
    print("0 - Kilépés")
    print("1 - Új tanulók felvétele")
    print("2 - Tanulók kilistázása")
    print("3 - Tanulók mentése fájlba")
    print("4 - Tanulók betöltése fájlból")
    valasztott=input("Válassz egy menüpontot: ")
    return valasztott

def fajlBetoltes():
    tanulok.clear()
    if exists(fajl):
        file = open(fajl, "r", encoding="utf-8")
        for row in file:
            tanulok.append(row.strip())
        file.close()
        print("A fájl betöltés sikeres.")
        input("tovább...")

def tanulokKiir():
    print("Tanulók: ")
    for tanulo in tanulok:
        print(f"\t{tanulo}")