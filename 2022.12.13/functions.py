from data import Varos
from typing import List

varosokLista:List[Varos]=[]

def loadFile():
    file=open("varosok.txt", "r", encoding="UTF-8")
    file.readline()
    for sor in file:
        varosokLista.append(Varos(sor))
    file.close()

def indiaiLakossa():
    osszeg=0
    for item in varosokLista:
        if item.Orszag == "India":
            osszeg+=item.Lakossag*1000
    return osszeg

def legnagyobbVaros():
    maxPoz=0
    for i in range(len(varosokLista)):
        if varosokLista[i].Lakossag > varosokLista[maxPoz].Lakossag:
            maxPoz=i
    return maxPoz

def MagyarKereses():
    for item in varosokLista:
        if item.Orszag=="Magyarország":
            return "van magyar város az adatok között"
    return "nincs magyar város"

def egySzokoz():
    db=0
    for item in varosokLista:
        if len(item.Nev.split(" "))==2:
            db+=1
    return db

def statisztika():
    stat={}
    for item in varosokLista:
        if item.Orszag in stat.keys():
            stat[item.Orszag]
        else:
            stat[item.Orszag]=1
    
    for key, value in stat.items():
        if value>6:
            print(f"\t{key} - {value} db")

def kinaiFajba():
    file=open("kina.txt", "w",encoding="UTF-8")
    for item in varosokLista:
        if item.Orszag="Kina":
            file.write(f"{item.nev};{item.Lakossag}\n")
    file.close()