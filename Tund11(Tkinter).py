from tkinter import *
from Tund10Matplotlib import *
global värv,tekst
def värvi_valik():

    värv="white"
    if tekst.get()!="":
        tekst.configure(bg="yellow")
        värv=tekst.get()
    else:
        tekst.configure(bg="red")
    return värv

def figuur(värv:str):
    valik=var.get()
    #värv=värvi_valik()
    if valik==1:
        Prillid(värv)
    elif valik==2:
        Vaal(värv)
    else:
        Vihmavari()
        print("Joonestan hiljem")

aken=Tk()
aken.geometry("800x400")
aken.title("Graafikud")
pealkiri=Label(aken,text="Erinevad piltid Matplotlib abil",font="Calibri 24",fg="green",bg="yellow",pady=20,width=100)
var=IntVar()
r1=Radiobutton(aken,text="Prillid",font="Calibri 18",variable=var,value=1,command=lambda:figuur(värv=värvi_valik()))
r2=Radiobutton(aken,text="Vaal",font="Calibri 18",variable=var,value=2,command=lambda:figuur(värv=värvi_valik()))
r3=Radiobutton(aken,text="Vihmavari",font="Calibri 18",variable=var,value=3,command=lambda:figuur(värv=värvi_valik()))
tekst=Entry(aken,font="Calibri 24",fg="green",bg="yellow",width=50)
nupp=Button(aken, text="Värvi valik",font="Calibri 24",command=värvi_valik())


pealkiri.pack() # place(x=...,y=...), grid(column=..., row=...)
tekst.pack()
nupp.pack()
r1.pack()
r2.pack()
r3.pack()
aken.mainloop()