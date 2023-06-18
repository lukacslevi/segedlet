# faktoriális

print(f"Faktoriális: ")

n = int(input("\nn: "))

faktorialis = 1
i=n
while i>0:
    faktorialis*=i
    i-=1
print(f"{n}! = {faktorialis}")