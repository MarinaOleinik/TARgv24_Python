#Ül 15
for read in range(20):
    for rida in range(10):
        print('{:>3}'.format(rida**2), end="")
    print()
print()

#Ül 16
for j in range(1,10):
    for i in range(1,10):   
        if i==j:
            print(j,end=" ")
        else:
            print("0", end=" ")
    print()
    
print()
#Ül 4
for i in range(10,21,1):
    print(i**2, end=";")

print()

#Ül 3
p=1
for j in range(8):
    while True:
        try:
            arv=float(input(f"Sisesta {j+1} arv:"))
            break
        except:
            print("On vaja arv")
    if arv>0:
        p*=arv
    else:
        print("Korrutame arvud rohkem kui 0")
    print(f"{j+1}. samm korrutis= {p}")
print(f"Lõpptulemus on {p}")



#Ül 2
while True:
    try:
        A=int(input("Sisesta A:"))
        break
    except:
        print("On vaja naturaalne arv")
summa=0
if A>0:
    for i in range(1,A+1,1):
        summa+=i                #summa=summa+i
        print(f"{i}. samm summa={summa}")
    print(f"Vastus {summa}")

