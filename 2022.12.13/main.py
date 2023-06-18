from functions import *

loadFile()
print(f"Városok száma: {len(varosokLista)}")
print(f"Indiai lakosság: {indiaiLakossa}")
print("a legnagyobb város adatai:")
print(f"név: {varosokLista[legnagyobbVaros()].Nev}")
print(f"ország: {varosokLista[legnagyobbVaros()].Orszag}")
print(f"Lakosság: {varosokLista[legnagyobbVaros()].Lakossag} ezer fő")