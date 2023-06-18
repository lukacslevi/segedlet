#számok kiírása intervallumon

i=1
while i<=100:
    print(i, end=' ')
    i+=1 #i növelése egyesével

#-----------------------------------
#véletlen szám
from random import randint
elso_dobas = randint(1, 6)
masodik_dobas = randint(1,6)

while elso_dobas!=6 or masodik_dobas!=6:
    print(f"{elso_dobas},{masodik_dobas}")
    elso_dobas = randint(1,6)
    masodik_dobas = randint(1,6)