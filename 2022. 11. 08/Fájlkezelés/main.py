from functions import fajlBetoltes, tanulokKiirasa, menu,ujTanulo, mentesFajlba, tanuloTorlese
from os import system
from data import tanulok #tanulok lista

valasztott=''
while valasztott!='0':
    system('cls')
    valasztott=menu()
    if valasztott=='1':
        system('cls')
        ujTanulo()
    elif valasztott=='2':
        system('cls')
        tanulokKiirasa()
        input('Tovább...')
    elif valasztott=='3':    
        system('cls')
        mentesFajlba()
    elif valasztott=='4':
        tanulok.clear()
        fajlBetoltes()
    elif valasztott=='5':
        fajlBetoltes()
    elif valasztott=='6':
        system('cls')
        tanuloTorlese()
