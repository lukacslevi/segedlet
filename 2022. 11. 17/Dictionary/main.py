from functions import *

loadCars()
choice=""
while choice !="0":
    choice=menu()
    if choice=="1":
        addNewCar()
    elif choice=="2":
        printAllCars()
    elif choice=="3":
        deleteCar()