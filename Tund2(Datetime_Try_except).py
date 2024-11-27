from datetime import *
from calendar import *
from random import *
from math import *

#Ülesanne 1
paevadekogus=monthrange(2024,11)[1] #calendar modulist
print(paevadekogus)

tana=date.today() #nimetus()-funktsioon 
tanaf=date.today().strftime("%B %d, %Y")

print(f"Tere! Täna on {tanaf}")
d=tana.day #nimetus - omadus 27
m=tana.month
y=tana.year
print(d)
print(m)
print(y)

detsP=monthrange(2024,12)[1] #31
novP=monthrange(2024,11)[1] #30
jaak=detsP+novP-d
jaak2=novP-d
print(f"Aasta lõpuni on {jaak}")
print(f"Kuu lõpuni on {jaak2}")

#Ülesanne 2
vastus1=3 + 8 / (4 - 2) * 4
vastus2=3 + 8 / 4 - 2 * 4
vastus3=(3 + 8) / (4 - 2) * 4
vastus4=round((3 + 8) / (4 - 2) * 4)
print(vastus1,"\n",vastus2,"\n",vastus3,"\n",vastus4)

#Ülesanne 3
#1 variant
try:
    R=float(input("Sisesta R: "))
    Sk=pi*R**2
    Lk=2*pi*R
    Skv=(2*R)**2
    Lkv=2*R*4
    print(f"Ringi pindala on {Sk}\nRingi ümnbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}\n")
except:
    print("On vaja number!")

#2 variant  
R=round(random()*100) #0.0...1.0
print(f"R={R}")
Sk=pi*R**2
Lk=2*pi*R
Skv=(2*R)**2
Lkv=2*R*4
print(f"Ringi pindala on {Sk}\nRingi ümnbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}\n")