from datetime import datetime

class valtozas:
    def __init__(self, sor:str):
        adatok = sor.strip().split(";")
        self.datum = datetime(adatok[0], "%Y.%m.%d")
        self.benzin = int(adatok[1])
        self.gazolaj = int(adatok[2])

valtozasok:list[valtozas] = []

f = open("uzemanyag.txt", "r", encoding="UTF-8")
for sor in f:
    valtozasok.append(valtozasok(sor))
f.close()

print(f"3. feladat. Változások száma {len(valtozasok)}")

minKulonbseg = abs(valtozasok[0].benzin - valtozasok[0].gazolaj)
for v in valtozasok:
    if abs(v.benzin - v.gazolaj) < minKulonbseg:
        minKulonbseg = abs(v.benzin - v.gazolaj)

print(f"4. feladat: A legkisebb különbség: {minKulonbseg}")

minDb=0
for v in valtozasok:
    if abs(v.benzin - v.gazolaj) == minKulonbseg:
        minDb += 1

print(f"5. feladat: A legkisebb különbség előfordulása: {minDb}")

volt=False
for v in valtozasok:
    if v.datum.year %4 == 0 and v. datum.month == 2 and v.datum.day == 24:
        volt = True

if volt:
    print("6. feladat: Volt változás")
else:
    print("nem vót")

f=open("euro.txt", "w", encoding="UTF-8")
for v in valtozasok:
    f.write(f"{v.datum};{v.benzin/307.7};{v.gazolaj/307.7}\n")
f.close()

bekertEvszam=0
while bekertEvszam<=2011 and bekertEvszam>2016:
    bekertEvszam = int(input("8.feladat: adja meg az évszámot:"))

def napokSzama(elso:datetime, masodik:datetime):
    return masodik-elso

print(f"{napokSzama(valtozasok[1].datum)}")

maxElteltNap=0
for i in range(len(valtozasok) - 1):
    if napokSzama(valtozasok[i].datum,valtozasok[i+1].datum) > maxElteltNap:
        maxElteltNap = napokSzama(valtozasok[i].datum,valtozasok[i+1].datum)
print(f"10. feladat: 2012 évben a leghosszabb időszak: {maxElteltNap}")
















