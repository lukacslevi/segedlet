from data import *

def fajlBeolvasas(fajlnev):
    f=open(fajlnev, "r", encoding="UTF-8")
    kiinduloMagassag=int(f.readline())
    for sor in f:
        szakaszok.append(Szakasz(sor))
    f.close()
    return kiinduloMagassag

def teljesHossz():
    hossz=0
    for item in szakaszok:
        hossz+=item.tavolsag
    return hossz

def legrovidebb():
    minPoz=0
    for i in range(1, len(szakaszok)):
        if szakaszok[i].tavolsag<szakaszok[minPoz].tavolsag:
            minPoz=i
    return minPoz

def legmagasabb(induloMagassag):
    magassag=induloMagassag
    for item in szakaszok:
        magassag=magassag+item.emelkedes-item.lejtes
        item.celMagassag = magassag

    maxPoz=0
    for i in range(1, len(szakaszok)):
        if szakaszok[i].celMagassag > szakaszok[maxPoz].celMagassag:
            maxPoz = i
    return maxPoz