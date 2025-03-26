from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks
from random import *
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")
tahvel.grid()

# üksik kriips (x0, y0, x1, y1)
tahvel.create_line(30, 40, 300, 40)

# ühendatud kriipsud (suvaline arv koordinaatide paare)
tahvel.create_line(30,60,  300,60,  300,100,  60,100)

# võimalik on muuta joone paksust (width) ja sisu värvi (fill)
tahvel.create_line(30, 130, 300, 130, width=4, fill="red")

# teistsugune joone stiil
tahvel.create_line(30, 150, 300, 150, width=5, dash=(5, 1, 2, 1), arrow=LAST)

# tõmbab kriipsud, ühendab otsapunktid ja värvib sisu
# värve saab määrata ka rgb komponentidena
# vt. http://www.colorpicker.com/
tahvel.create_polygon(30,160,  300,160,  300,200,  60,200, fill="#95BD9D")

# ristkülik
tahvel.create_rectangle(30,260,  300,300)

# ovaal
tahvel.create_oval(30,260,  300,300, width=2, outline="blue", fill="wheat")

# proovi liigutada hiirt selle ovaali kohale
tahvel.create_oval(330, 330, 400, 400, fill="gray", activefill="pink")

# kui soovid teksti esitamisel ise fonti valida, siis tuleb enne vastav font luua
suur_font = font.Font(family='Helvetica', size=32, weight='bold')
tahvel.create_text(30, 500, text="Tere!", font=suur_font, anchor=NW)
tahvel.delete("all")
colors = ["black",
           "cyan",
           "magenta",
           "red",
           "blue",
           "gray",
           "yellow"
           "green",
           "lightblue",
           "pink",
           "gold"]
x0=0
y0=0
x1=600
y1=600
p=2
for i in range(150):  
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    tahvel.create_oval(x0,y0,x1,y1, fill=choice(colors))
# tahvel.delete("all")
# x0=0
# y0=0
# x1=600
# y1=600
# p=0
# x_=600
# y_=600
# for i in range(20):      
#     x0+=p
#     y0+=p
#     x1-=p
#     y1-=p
#     tahvel.create_rectangle(x0,y0,x1,y1, fill="yellow")
#     tahvel.create_oval(x0,y0,x1,y1, fill="magenta")
#     x_-=2*p
#     y_-=2*p
#     p=int(((x_**2+y_**2)**(1/2)-x_)/2)
#     p=int(((p**2)/2)**(1/2))
raam.mainloop()

