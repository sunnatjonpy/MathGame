from tkinter import *
import random as r

oyna = Tk()
oyna.title("Math")
oyna.geometry("300x300")

random1 = r.randint(1,151)
random2 = r.randint(1,151)

pluss = random1+random2
minus = random1-random2
kopp = random1*random2
boll = random1/random2

l = [pluss,minus,kopp,boll]
def plus():
    yigindi = random1+random2
    amal.config(text="+")
    result.config(text=yigindi)
    if result["text"]==resultl["text"]:
        result.config(text="Correct!",fg='green')
    else:
        result.config(text="Incorrect!",fg='red')
def minus():
    ayirma = random1-random2
    amal.config(text="-")
    result.config(text=ayirma)
    if result["text"]==resultl["text"]:
        result.config(text="Correct!",fg='green')
    else:
        result.config(text="Incorrect!",fg='red')

def kop():
    kopaytma = random1*random2
    amal.config(text="*")
    result.config(text=kopaytma)
    if result["text"]==resultl["text"]:
        result.config(text="Correct!",fg='green')
    else:
        result.config(text="Incorrect!",fg='red')

def bol():
    bolinma = random1/random2
    amal.config(text="/")
    result.config(text=bolinma)
    if result["text"]==resultl["text"]:
        result.config(text="Correct!",fg='green')
    else:
        result.config(text="Incorrect!",fg='red')
   
titlee = Label(oyna,text="Math Game",fg="blue", font="Broadway  15")
titlee.pack()

f_son = Label(text=random1)
f_son.place(x=50, y=40,width="80")
s_son = Label(text=random2)
s_son.place(x=110,y=40,width="80")

amal = Label(text="x")
amal.place(x=115,y=40)

teng = Label(text="=")
teng.place(x=170,y=40)

resultl = Label(text=r.choice(l))
resultl.place(x=190,y=40)

hisoblash1 = Button(oyna,text="+",command=plus,bg='greenyellow')
hisoblash1.place(x=50,y=70,width="40")
hisoblash2 = Button(oyna,text="-",command=minus,bg='greenyellow')
hisoblash2.place(x=100,y=70,width="40")
hisoblash3 = Button(oyna,text="/",command=bol,bg='greenyellow')
hisoblash3.place(x=150,y=70,width="40")
hisoblash4= Button(oyna,text="*",command=kop,bg='greenyellow')
hisoblash4.place(x=200,y=70,width="40")

result = Label(text="Result",font="Stencil 15")
result.place(x=90,y=120,width="120",height="20")

oyna.mainloop()
