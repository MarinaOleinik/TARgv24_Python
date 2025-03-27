from random import *
def summa3(arv1:int,arv2:int,arv3:int)->int:
    """Tagastab kolme täisarvu summa

    :param int arv1: Esimene number
    :param int arv2: Teine number
    :param int arv3: Kolmas number
    :rtype: int

    """
    summa=arv1+arv2+arv3
    return summa

def arithmetic(a:float,b:float,t:str)->any:
    """Lihtne kalkulaator. 
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: arv1
    :param float b: arv2
    :param str t: atitmeetiline tehing
    :rtype: var Määramata tüüp(float or str)
    """
    if t in ["+","-","*","/"]:
        if b==0 and t=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a)+t+str(b))
    else:
        vastus="Tundmatu tehe"

    return vastus

def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine 
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus

    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

def square(a:float)->any:
    """
    """
    S=a**2
    P=4*a
    d=(2)**(1/2)*a
    return S,P,d
def square_text(a:float)->str:
    """
    """
    S=a**2
    P=4*a
    d=(2)**(1/2)*a
    
    return "Pindala\n"+str(S)+",Ümbermõõt\n"+str(P)+",Läbimõõt\n"+str(d)

def square_format(a:float)->str:
    """
    """
    S=a**2
    P=4*a
    d=(2)**(1/2)*a
    
    return f"Pindala {S},Ümbermõõt {P},Läbimõõt {d}"
#4
def season(param:int)->str:
    """
    """
    if 1<=param<=12:
        if param in [1,2,12]:
            v="talv"
        elif param>2 and param<6:
            v="kevad"
        elif 6<=param<=8:
            v="suvi"
        else:
            v="sügis"
    else:
        v="!!!!"
    return v
#5
def bank(a:float,years:int)->float:
    """

    """
    for i in range(years):
        a*=1.1
    return a
#6

def is_prime(a=randint(0,1000))->bool:
    """
    """
    print(a)
    v=True
    for i in range(2,a):
        if a%i==0:
            v=False
    
    return v
#7
def date(päev:int,kuu:int,aasta:int)->bool:
    """
    """

    if päev in range(1,31) and kuu in [1,3,5,7,8,10,12]:
        v=True
    elif päev in range(1,29) and kuu==2 and is_year_leap(aasta): # veel tingimus!
        v=True
    elif päev in range(1,30) and kuu in [2,4,6,9,11]:
        v=True
    else:
        v=False
    return v


def XOR_cipher(text:str, võti:int)->str:
    """Sõne kodeerimine ASCII võtiga 0-255.
    :param text: Sõne, mis on vaja kodeerida.
    :param võti: Võti on arv vahemikus 0-255.
    :rtype: Valmis sõne.
    """
    kodeeritud=""
    for symbol in text:
        kodeeritud+=chr(ord(symbol)^võti)
    return kodeeritud
def XOR_uncipher(kodeeritud_text:str, võti:int)->str:
    """
    Dekodeerimine
    """
    dekodeeritud_text= ''.join(chr(ord(char) ^ võti) for char in kodeeritud_text)
    return dekodeeritud_text
#9
def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
#10
def min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)
#11
def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result