# lista
import random

lista=[]
elemszam=int(input("Hány elemű legyen a lista?"))

for i in range(elemszam):
    #print(i)
    lista.append(random.randint(0,100))
print(lista)
lista.sort()
print(f"rendezve: {lista}")
print(f"A lista 5. eleme: {lista[4]}")
print(f"A listában " + str(len(lista)) + " elem van")
print(f"A lista utolsóü eleme: {lista[-1]}")
print(f"A list aelső 5 eleme: {lista[0:5]}")
print(f"{lista[5:-2]}")
lista2=lista[0:5]