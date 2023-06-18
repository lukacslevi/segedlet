from functions import fajlBetoltes, tanulokKiir, menu
from os import system

menu()
fajlBetoltes()
tanulokKiir()

valasztott=""
while valasztott != "0":
    system("cls")
    valasztott=menu()
    if valasztott=="2":
        system("cls")
        tanulokKiir()
        input("tovább...")
    elif valasztott=="4":
        fajlBetoltes()