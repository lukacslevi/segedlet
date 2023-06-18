class CBadás:
    def __init__(self, line:str):
        data = line.strip().split(";")
        self.ora = int(data[0])
        self.perc = int(data[1])
        self.adasDb = int(data[2])
        self.nev = data[3]

adasok:list[CBadás] = []

f = open("cb.txt", "r", encoding="UTF-8")
f.readline()
for sor in f:
    adasok.append(CBadás(sor))
f.close()

print("3. feladat: CB-Rádió")
print(f"3.2 feladat: Bejegyzések száma: {len(adasok)} db")

sanyi = 0
for item in adasok:
    if item.nev == "Sanyi":
        sanyi += 1

print(f"3.3 feladat: Sanyihoz tartozó bejegyzések: {sanyi} db")

max = 0
for item in adasok:
    if item.adasDb > max:
        max = item.adasDb

stat = {}
for item in adasok:
    if item.adasDb == max:
        time = str(item.ora) + ":" + str(item.perc)
        stat[time] = item.nev

print("3.4 feladat: A legtöbb adás:")
for key, value in stat.items():
    print(f"\tIdő: {key} Darab: {max} Név: {value}")

f = open("cb2.txt", "w", encoding="UTF-8")
f.write("Kezdes;Nev;AdasDb\n")
for item in adasok:
    f.write(f"{item.ora * 60 + item.perc};{item.nev};{item.adasDb}\n")