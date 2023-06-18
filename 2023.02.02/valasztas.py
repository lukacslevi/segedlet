class jelolt:
    def __init__(self, sor:str):
        adatok = sor.strip().split(" ")
        self.kerulet = int(adatok[0])
        self.szavazatok = int(adatok[1])
        self.nev = adatok[2] + " " + adatok[3]
        self.part = adatok[4]

jeloltek:list[jelolt] = []

f = open("szavazatok.txt", "r", encoding="UTF-8")
for sor in f:
    jeloltek.append(jelolt(sor))
f.close()

print(f"2. feladat: A választáson {len(jeloltek)} képviselőjelölt indult.")

bekertNev = input("3. feladat: Képvisalő neve: ")
talalt = False
for item in jeloltek:
    if item.nev == bekertNev:
        talalt = True
        print(f"A jelölt a {item.kerulet}-s számú körzetben indult.")
        print(f"A kapott szavazatok száma: {item.szavazatok}")
if not talalt:
    print("\t nincs ilyen nber")

szavazok=0
for item in jeloltek:
    szavazok += item.szavazatok
print(f"4. feladat: {szavazok} szavazó a jogosultak {szavazok/12345*100:.2f}%-a vett részt.")

maxpoz=0
for i in range(len(jeloltek)):
    if jeloltek[i].szavazatok > jeloltek[maxpoz].szavazatok:
        maxpoz = i

if jeloltek[maxpoz].part=="-":
    print(f"független: {jeloltek[maxpoz].szavazatok} szavazat")
else:
    print(f"{jeloltek[maxpoz].part}")

stat={}
for item in jeloltek:
    if item.part in stat.keys():
        stat[item.part] += item.szavazatok
    else:
        stat[item.part] = item.szavazatok

for key, value in stat.items():
    print(f"{key}: {value} szavazat")

f=open("tisz.csv", "w", encoding="utf-8")
for item in jeloltek:
    if item.part == "TISZ":
        f.write()