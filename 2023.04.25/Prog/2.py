from random import randint
numbers = []

def ezprim(number):
    for i in range(2,number):
        if (number%i) == 0:
            return False
    return True

for i in range(10):
    numbers.append(randint(10, 99))

print(numbers)

for item in numbers:
    noprime = True
    if ezprim(item):
        print("Van prímszám a listában!")
        noprime = False
        break

if noprime == True:
    print("Nincs prímszám a listában!")
