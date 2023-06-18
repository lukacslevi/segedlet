#listák

üresLista=[] 
print(üresLista)

listaKezdőértékkel=[4,6,1,2,5,8,3]
print(listaKezdőértékkel)

gyümölcsLista=["alma","körte","barack","eper"]
print(gyümölcsLista)

#egy elem elérése(index)
print(gyümölcsLista[2])
print(gyümölcsLista[0])

#egy teljes lista kiírása
for item in listaKezdőértékkel:
    print(item)

# lista elemszáma
print(f"a gyümölcsök száma: {len(gyümölcsLista)}")

for i in range(0,len(gyümölcsLista)):
    print(f"{i}. elem: {gyümölcsLista[i]}")

ujGyumolcs=input("Kérek egy gyümölcsöt: ")
gyümölcsLista.append(ujGyumolcs)

gyümölcsLista.remove('alma')
print(gyümölcsLista)

listaKezdőértékkel.sort()
listaKezdőértékkel.sort(reverse=True)

print(listaKezdőértékkel)

szam = int(input('Kérek egy számot, megmondom, benne van-e a listában: '))
if szam in listaKezdőértékkel:
    print('benne van!')
else:
    print('nincs benne!')

#listaelem módosítás
gyümölcsLista[0]="narancs"
print(gyümölcsLista)