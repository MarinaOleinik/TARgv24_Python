from random import *  #*-kõik funktsioonid, randint as rd funktsioonide ümbernimetus
#import random -> random.randint()
from math import *
from tkinter import * #pi kasutamiseks


#Ülesanne 1
print("Tere tulemast!")
nimi=input("Mis on sinu nimi? ").capitalize() #lower()-aaa,upper()-AAA,capitalize()-Aaa
print("Tere tulemast! Tervitan sind ", nimi) 
print("Tere tulemast! Tervitan sind "+ nimi)
try:
    vanus=int(input("Kui vana sa oled? "))
    print("Tere tulemast! Tervitan sind "+nimi+" Sa oled ",vanus,"aastat vana")
    print(f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastat vana")
except:
    print("On vaja numbreid sisestda!")




#Ülesanne 2
vanus = 18
eesnimi = "Jaak" 
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))

#Ülesanne 3
kokku=randint(1,1000)
print(f"Kokku on {kokku} kommi")
kommi=int(input("Mitu kommi sa tahad? "))
kokku=kokku-kommi
print(f"Jääk on {kokku} kommi")

#Ülesanne 4
print("Läbimõõdu leidmine ")
#l-ümbermõõt
l=float(input("Ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")
