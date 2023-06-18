#fibonacci

elozo_elotti = 0
elozo = 1 

print(elozo_elotti, end=' ')
print(elozo_elotti, end=' ')

for i in range(2, 40):
    osszeg=elozo+elozo_elotti
    print(osszeg, end=' ')
    elozo_elotti =elozo
    elozo = osszeg