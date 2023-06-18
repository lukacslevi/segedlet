def terulet(a,b):
    ter=a*b
    if ter < 100:
        raise ValueError("túl kicsi a biga")
    return ter

print("terület számítás")

while True:
    a=float(input("Kérem adja meg a telek szélességét: "))
    if a==-1:
        break
    b=float(input("Adja meg a hosszúságát: "))
    if b==-1:
        break
    try:
        print("telek területe")
    except ValueError as error:
        print(error)