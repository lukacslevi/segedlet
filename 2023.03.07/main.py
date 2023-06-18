from functions import *

readFile()
print(versenyzok[1].helyszin)
print(f"4. feladat: Real Madrid: {realmadrid()}")
if dontetlen():
    print("vót")
else:
    print("nem vót")

print("5. feladat: barcelonai csapat neve: ", end="")
barcelonaNev()
print("6. feladat: ")
meccsek()
stadionok()