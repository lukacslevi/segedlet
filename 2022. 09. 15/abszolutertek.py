# abszolútérték meghatározása
print("Kérem adjon meg egy számot!")

def abszolut(number):
    if number < 0:
        number = number *-1
    return number

szam=int(input("Szám="))

# if szam < 0:
#     szam = -szam 

szam=abszolut(szam)

print(f"A szám abszolútértéke: {szam}")