from data import cars
from os import system

filename="cars.csv"
cimsor=""

def menu():
    system("cls")
    print("0 - Kilépés")
    print("1 - Új autó felvétele")
    print("2 - Listázás")
    print("3 - Autó törlése")
    return input("Válassz: ")

def loadCars():
    file=open(filename, "r", encoding="utf-8")
    global cimsor
    cimsor = file.readline().strip()
    for row in file:
        splitted=row.strip().split(";")
        cars[splitted[0]]=int(splitted[1])
    file.close

def printAllCars():
    system("cls")
    print("Autók listája:\n")
    for key,value in cars.items():
        print(f"{key} - {value} Hp.")
    input()

def addNewCar():
    system("cls")
    print("Új autó")
    car=input("Autó típusa: ")
    hp=input("Teljesítmény: ")
    cars[car] = hp
    saveCarToFile(car,hp)
    input("Autó felvéve.")

def saveCarToFile(car,hp):
    file=open(filename, "a", encoding="utf-8")
    file.write(f"\n{car};{hp}")
    file.close()

def deleteCar():
    system("cls")
    print("Autó törlése")
    car=input("A törlendő autó típusa: ")
    if car in cars:
        cars.pop(car)
        saveAllToFile()
        input("Sikeresen törölve.")
    else:
        input("Nincs ilyen autó.")

def saveAllToFile():
    file=open(filename, "w", encoding="utf-8")
    file.write(cimsor)
    for key, value in cars.items():
        file.write(f"\n{key};{value}")
    