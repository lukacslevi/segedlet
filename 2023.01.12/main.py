from functions import *

readFile()
print(f"3. feladat: Hegycsúcsok száma: {len(hegyek)} db")
print(f"4. feladat: Hegycsúcsok átlagos magassága: {atlag()} m")
print(f"5. feladat: A legmagasabb hegycsúcs adatai:")
print(f"\t Név: {hegyek[highest()].hegycsucs}")
print(f"\t Hegység: {hegyek[highest()].hegyseg}")
print(f"\t Magasság: {hegyek[highest()].magassag} m")

num=int(input("6. feladat: Kérek egy magasságot: "))
if int(hegyek[highest()].magassag) > num:
    print(f"Van {num} m-nél magasabb hegycsúcs a {hegyek[highest()].hegycsucs}")

print(f"7. feladat: 3000 lábnál magasbb hegycsúcsok száma: {higher()}")
getHeights(getMountains())
print(f"9. feladat: bukk-videk.txt")
writeBukk()

