from functions import *

print("1. feladat: A háromszög szerkeszthetősége")
print("Kérem a háromszög oldalait!")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if check(a,b,c):
    print("A háromszög megszerkeszthető!")
else:
    print("A háromszög nem szerkeszthető a megadott adatokkal!")

##########################
print("\n")


print("2. feladat: Tökéletes számok")
print("Kérek két tökéletets számot:")
tol = int(input("tól = "))
ig = int(input("ig = "))
print(f"Tökéletes számok {tol} és {ig} között: ")
if len(tokeletes(tol, ig)) == 0:
    print("A megadott tartományban nincsen tökéletes szám!")
else:
    print(tokeletes(tol, ig))

##########################
print("\n")


readFile()
print(f"3.2 feladat: Futók száma: {len(eredmenyek)}")
print(f"3.3 feladat: Célba érkező női sportolók: {no()}")
