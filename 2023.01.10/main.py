from functions import *

FajlBeolvas()
print(f"1. feladat: {len(vbOrszagok)}\n")
print(f"2. feladat: 2018-as vb csapatai: ")
UtolsoVBnVolt()
print()

print(f"3. feladat: A BeNeLux országok összesen {BeNeLux()} alkalommal vettek részt a VB-n.")

print(f"4. feladat: Az első VB-t {ElsoVB()}-ban rendezték\n")

print(f"5. feladat: Eddig {NyertesDb()} ország csapata volt világbajnok.")

print(f"6. feladat: Szlovákia legjobb eredmények: {Szlovakia()}")

orszag="Magyarország"
if Kintvolte(orszag):
    print(f"7. feladat: {orszag} ott volt a VB-n")
else:
    print(f"7. feladat: {orszag} nem volt ott VB-n.")

Legtobbszor()
print("8. feladat: legtobbszor.txt kész!")