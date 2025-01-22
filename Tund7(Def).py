from Tund7Modul import *

#8
s=input("Sisesta sõne kodeerimiseks: ")
v=int(input("Võti: "))
kood=XOR_cipher(s,v)
print(kood)
sõne=XOR_uncipher(kood,v)
print(sõne)

#3
S,P,D=square(10)
#1
a=int(input("Sisesta arv1: "))
b=int(input("Sisesta arv2: "))
c=input("Sisesta arv3: ")
#Näidis
vastus=summa3(a,b,int(c))
print(vastus)

