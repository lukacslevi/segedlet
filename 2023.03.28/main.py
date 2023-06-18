class Versenyzo:
    def __init__(self, sor:str):
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.orszag = adatok[1]
        self.techpsz = float(adatok[2])
        self.kompsz = float(adatok[3])
        self.hibapsz = float(adatok[4])

versenyzok:list[Versenyzo] = []
versenyzok2:list[Versenyzo] = []


f = open("donto.csv", "r", encoding="UTF-8")
f.readline()
for sor in f:
    versenyzok.append(Versenyzo(sor))
f.close()

f = open("rovidprogram.csv", "r", encoding="UTF-8")
f.readline()
for sor in f:
    versenyzok2.append(Versenyzo(sor))
f.close()

#2
print("2. feladat:")
print(f"\tA rövidprogramban {len(versenyzok2)} induló volt")

#3
print("3. feladat:")
for item in versenyzok2:
    if item.orszag == "HUN":
        print(f"\tA magyar versenyző bejutott a kűrbe")
        break

#4
def ÖsszPontszám(nev:str):
    psz=0
    if nev in versenyzok:
        for item in versenyzok:
            if item.nev == nev:
                psz += item.kompsz + item.techpsz
        for item in versenyzok2:
            if item.nev == nev:
                psz += item.kompsz + item.techpsz       
    else:
        for item in versenyzok2:
            if item.nev == nev:
                psz += item.kompsz + item.techpsz
    return psz

keresett = input("Kérem a versenyző nevét: ")
volt = False
for item in versenyzok2:
    if item.nev == keresett:
        volt = True
        break
if not volt:
    print("NINCS ILYEN BAZD+")

#6
print(f"A versenyző összpontszáma: {ÖsszPontszám(keresett)}")

#7

