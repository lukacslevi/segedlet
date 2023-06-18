from data import *

def readFile():
    f = open("eredmenyek.txt", "r", encoding="UTF-8")
    f.readline()
    for sor in f:
        versenyzok.append(Versenyzo(sor))
    
def realmadrid():
    hazai = 0
    idegen = 0
    for item in versenyzok:
        if item.hazai == "Real Madrid":
            hazai += 1
        elif item.idegen == "Real Madrid":
            idegen += 1
    return f"Hazai: {hazai}, Idegen: {idegen}"

def dontetlen():
    for item in versenyzok:
        if item.hazai_pont == item.idegen_pont:
            return True
        
def barcelonaNev():
    for item in versenyzok:
        if "Barcelona" in item.idegen:
            print(item.idegen)
            break

def meccsek():
    for item in versenyzok:
        if item.idopont == "2004-11-21":
            print(f"\t{item.hazai}-{item.idegen} ({item.hazai_pont}:{item.idegen_pont})")

stadionok = {}
def stadionok():
    for item in versenyzok:
        stadionok[item.helyszin] += 1