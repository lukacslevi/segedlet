szelesseg=int(input("Hány méter széles a terület?: "))
hosszusag=int(input("Hány méter hosszú a terület?: "))
terulet=szelesseg*hosszusag
teruletNegyszogol=terulet*0.2780364289

print("A felszántandó terület: ")
print(f"\tMérete: {terulet} m2")
print(f"Mérete (négyszögöl): {teruletNegyszogol}")
print(f"Munkadíj: {teruletNegyszogol * 0.07+5000:.0f} Ft.")