from ast import Lambda
from tkinter import *
from tkinter import messagebox
from math import *
import numpy as np
import matplotlib.pyplot as plt

graf=False
def Lahenda():
    global lbl_vastus,lbl_a, lbl_b, lbl_c, graf
    try:
        a=float(lbl_a.get())
        b=float(lbl_b.get())
        c=float(lbl_c.get())
        D=b*b-4*a*c
        if D>0:
            x1_=round((-1*b+sqrt(D))/(2*a),2)
            x2_=round((-1*b-sqrt(D))/(2*a),2)
            t=f"X1={x1_}, \nX2={x2_}"
            graf=True
        elif D==0:
            x1_=round((-1*b)/(2*a),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="Корней нет"
            graf=False
        lbl_vastus.configure(text=f"D={D}\n{t}")
    except Exception as e:
        messagebox.showerror("Viga!",e)
    return graf

def Graafik(graf:bool):
    global lbl_vastus,lbl_a, lbl_b, lbl_c
    if graf==True:
        a=float(lbl_a.get())
        b=float(lbl_b.get())
        c=float(lbl_c.get())
        x0=(-b)/2*a
        y0=a*x0*x0+b*x0+c
        x=np.arange(x0-15,x0+15,1)#min,max,step
        y=a*x*x+b*x+c
        fig=plt.figure()
        plt.plot(x,y,'r-d')
        plt.title("Ruutvõrrand")
        plt.ylabel('Y')
        plt.xlabel('X')
        plt.grid(True)
        plt.show()
    else:
        messagebox.showerror("Viga!","Ei saa graafik näha")
def Aken_pack():
    global lbl_vastus,lbl_a, lbl_b, lbl_c
    aken=Tk()
    aken.geometry("650x260")
    aken.title("Ruutvõrrand")
    aken.resizable(False, False)
    f1=Frame(aken,width=650,height=260)
    f1.pack(side=TOP)
    
    lbl=Label(f1,text="Ruutvõrrandite lahendamine", font="Calibri 26",fg="green",bg="lightblue")
    lbl.pack(side=TOP)
    lbl_vastus=Label(f1,text="Lahendamine",height=4,width=60,bg="yellow")
    lbl_vastus.pack(side=BOTTOM)
    lbl_a=Entry(f1,font="Calibri 26",fg="green",bg="lightblue", width=3)
    lbl_a.pack(side=LEFT)
    x2=Label(f1,text="x^2+",font="Calibri 26",fg="green",padx=10)
    x2.pack(side=LEFT)
    lbl_b=Entry(f1,font="Calibri 26",fg="green",bg="lightblue", width=3)
    lbl_b.pack(side=LEFT)
    x=Label(f1,text="x+",font="Calibri 26",fg="green",padx=10)
    x.pack(side=LEFT)
    lbl_c=Entry(f1,font="Calibri 26",fg="green",bg="lightblue", width=3)
    lbl_c.pack(side=LEFT)
    y=Label(f1,text="=0",font="Calibri 26",fg="green",padx=10)
    y.pack(side=LEFT)
    btn_lahenda=Button(f1, text="Lahenda",font="Calibri 26",fg="green",command=Lahenda)

    btn_lahenda.pack(side=LEFT)
    btn_graafik=Button(f1, text="Graafik",font="Calibri 26",fg="green",command=lambda:Graafik(graf))
    btn_graafik.pack(side=LEFT)
    aken.mainloop()
def Aken_grid():
    global lbl_vastus,lbl_a, lbl_b, lbl_c
    aken=Tk()
    aken.geometry("650x260")
    aken.title("Ruutvõrrand")
    aken.resizable(False, False)
    f1=Frame(aken,width=650,height=260)
    f1.pack(side=TOP)   
    lbl=Label(f1,text="Ruutvõrrandite lahendamine", font="Calibri 26",fg="green",bg="lightblue")
    lbl.grid(row=0, column=0,columnspan=8)
    lbl_vastus=Label(f1,text="Lahendamine",height=4,width=60,bg="yellow")
    lbl_vastus.grid(row=2, column=0,columnspan=8)
    lbl_a=Entry(f1,font="Calibri 26",fg="green",bg="lightblue", width=3)
    lbl_a.grid(row=1, column=0)
    x2=Label(f1,text="x^2+",font="Calibri 26",fg="green",padx=10)
    x2.grid(row=1, column=1)
    lbl_b=Entry(f1,font="Calibri 26",fg="green",bg="lightblue", width=3)
    lbl_b.grid(row=1, column=2)
    x=Label(f1,text="x+",font="Calibri 26",fg="green",padx=10)
    x.grid(row=1, column=3)
    lbl_c=Entry(f1,font="Calibri 26",fg="green",bg="lightblue", width=3)
    lbl_c.grid(row=1, column=4)
    y=Label(f1,text="=0",font="Calibri 26",fg="green",padx=10)
    y.grid(row=1, column=5)
    btn_lahenda=Button(f1, text="Lahenda",font="Calibri 26",fg="green",command=Lahenda)
    btn_lahenda.grid(row=1, column=6)
    btn_graafik=Button(f1, text="Graafik",font="Calibri 26",fg="green",command=lambda:Graafik(graf))
    btn_graafik.grid(row=1, column=7)
    aken.mainloop()

#Aken_pack()
Aken_grid()
