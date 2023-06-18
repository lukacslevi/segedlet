nevek=['Wojciech Nowicki',	'Eivind Henriksen',	'Paweł Fajdek',	'Mihajlo Kohan',	'Quentin Bigot',	'Nick Miller',	'Rudy Winkler',	'Valerij Pronkin',	'Eşref Apak',	'Javier Cienfuegos',	'Daniel Haugh',	'Serghei Marghiev']
dobasok=[82.52,	81.58,	81.53,	80.39,	79.39,	78.15,	77.08,	76.72,	76.71,	76.3,	76.22,	75.24]

#Hány döntős volt?
print(f"{len(nevek)} döntős volt a kalapácsvetés számban.")

#ki nyert
maxPoz=0
for i in range(1, len(dobasok)):
    if dobasok[i]>dobasok[maxPoz]:
        maxPoz=i
print(f"{nevek[maxPoz]} nyerte a versenyt {dobasok[maxPoz]} méteres dobással.")

#átlag
osszeg=0
for item in dobasok:
    osszeg+=item
print(f"A döntőban a dobások átlaga {osszeg/len(dobasok):.2f} m.")

#névhez tartozó dobás
bekertNev = input("Kérem adjon meg egy nevet: ")
i=0
while i<len(nevek) and nevek[i]!=bekertNev:
    i+=1
if i<len(nevek):
    print(f"\t{nevek[i]} {dobasok[i]} m-t dobott.")
else:
    print("\tNincs ilyen kalapácsvető!")

#hányan dobtak az átlag felett
db=0
for item in dobasok:
    if item>osszeg/len(dobasok):
        db+=1
print(f"{db} versenyző dobott az átlag felett")

#legrövidebb nevű versenyzők
minPoz=0
for i in range(1, len(nevek)):
    if len(nevek[i])<len(nevek[minPoz]):
        minPoz=i
print("legrövidebb nevű versenyzők: ")
for i in range(len(nevek)):
    if len(nevek[i])==len(nevek[minPoz]):
        print(nevek[i])

#--------------------------------------
szoveg=input("szöveg: ")
mgh="aáeéiíoóöőüűuú"

db=0
for i in range(0,len(szoveg)):
    if szoveg[i] in mgh:
        db+=1
print(f"A szövegben {db} magánhangzó van")
