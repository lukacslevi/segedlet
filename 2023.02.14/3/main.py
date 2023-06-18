from functions import *

readFile()
print(f"3. feladat: Az iskolába {len(tanulok)} tanuló jár.")

tanulokHosszal={}
for item in tanulok:
    tanulokHosszal[item.nev] = countName(item.nev)

legnagyobb = max(tanulokHosszal.values())
print(f"4. feladat: A leghosszabb ({legnagyobb} karakter) nevű tanuló(k):")
for key, value in tanulokHosszal.items():
    if value == legnagyobb:
        print(f"\t{key}") 


print(username(tanulok[0].szulev, tanulok[0].osztaly, tanulok[0].nev))
print(username(tanulok[-1].szulev, tanulok[-1].osztaly, tanulok[-1].nev))

tanulokAzonositoval={}
for i in range(len(tanulok)):
    tanulokAzonositoval[tanulok[i].nev] = username(tanulok[i].szulev, tanulok[i].osztaly, tanulok[i].nev)

print(tanulokAzonositoval)

keres = input("Kérek egy azonosítót: ")
for key, value in tanulokAzonositoval.items():
    if value == keres:
        print(key)