from functions import *

readFile()
print(f"3. feladat:\nPontszerző helyezések száma: {len(eredmenyek)}")

print(f"4. feladat:")
print(f"Arany: {helyezesekSzama(1)}")
print(f"Arany: {helyezesekSzama(2)}")
print(f"Arany: {helyezesekSzama(3)}")
print(f"Összesen: {helyezesekSzama(1)+helyezesekSzama(2)+helyezesekSzama(3)}")

print(f"5. feladat:\nOlimpiai pontok száma: {osszpont()}")

torna=sportagErmek("torna")
uszas=sportagErmek("uszas")
print("6. feladat")
if uszas>torna:
    print("Úszás sportágban szereztek több érmet")
elif uszas<torna:
    print("Torna sportágban szereztek több érmet")
else:
    print("Egyenlő az érmek száma")

fajlbaIras()

print("8. feladat")
print(f"Helyezés: {eredmenyek[maxLetszam()].helyezes}")