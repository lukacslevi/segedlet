import math

def prim(szam):
    for i in range(2, int(math.sqrt(szam))+1):
        if szam%i==0:
            return False
    return True

db =0 # 0 talált prímszám
szam=2

while db<50:
    if prim(szam):
        print(szam, end=' ')
        db+=1
    szam+=1