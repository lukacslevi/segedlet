import os

class Eu:
    def __init__(self, line:str):
        data = line.strip().split(";")
        self.orszag = data[0]
        self.csatlakozas = data[1]

orszagok:list[Eu] = []

f = open("EUcsatlakozas.txt", "r", encoding="UTF-8")
for line in f:
    orszagok.append(Eu(line))

# 3

print(f"3. feladat: EU tagállamainak száma: {len(orszagok)} db")

# 4

count=0
for item in orszagok:
    date = item.csatlakozas.split(".")
    if date[0] == "2007":
        count += 1

print(f"4. feladat: 2007-ben {count} ország csatlakozott.")

# 5

for item in orszagok:
    if item.orszag == "Magyarország":
        print(f"5. feladat: Magyarország csatlakozásának dátuma: {item.csatlakozas}")
        break

# 6

for item in orszagok:
    date = item.csatlakozas.split(".")
    if date[1] == "05":
        print("6. feladat: Májusban volt csatlakozás!")
        break


# 7

days = {}
for item in orszagok:
    date = item.csatlakozas.split(".")
    days[item.orszag] = date[0] * 365 + date[1] * 30 + date[2]

maxVal = 0
maxKey = ""
for key, value in days.items():
    if int(value) > maxVal:
        maxVal = int(value)
        maxKey = key

print(f"7. feladat: Legutoljára csatlakozott ország: {maxKey}")

# 8

print(f"8. feladat: Statisztika")

stats = {}
for item in orszagok:
    date = item.csatlakozas.split(".")
    if date[0] not in stats.keys():
        stats[date[0]] = 1
    else:
        stats[date[0]] += 1

for key, value in stats.items():
    print(f"\t{key} - {value} ország")
        