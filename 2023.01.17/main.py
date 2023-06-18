from functions import *

readFile()
print(f"3. feladat: Versenyzők száma: {len(versenyzok)}")

print(f"4. feladat: A női versenyzők aránya: {round(NoiVersenyzok(), 2)}")

print(f"Név: {versenyzok[noiBajnok()].Nev}")
print(versenyzok[39].osszpont())

stat()
ferfiPontok()