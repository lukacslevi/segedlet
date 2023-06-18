# megszerkeszthető-e a háromszög?

print("Kérem adja meg a háromszög oldalait!")

a_oldal = int(input("a oldal: "))
b_oldal = int(input("b oldal: "))
c_oldal = int(input("c oldal: "))

if a_oldal + b_oldal > c_oldal and a_oldal + c_oldal > b_oldal and b_oldal + c_oldal > a_oldal:
    print("A háromszög megszerkeszthető")
else:
    print("A háromszög nem megszerkeszthető")

#Logikai kapcsolatok

#ÉS
#      A     B      eredmény
#      0     0      
#      0     1
#      1     0
#      1     1