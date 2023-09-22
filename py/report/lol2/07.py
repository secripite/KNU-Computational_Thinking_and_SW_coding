from tkinter import *
import tkinter.ttk as atk


entval = 0
btnval = 0
comval = 0
radval = 0

def update():
    label1.config(text = str(int(entval) if entval != '' else 0 +btnval+comval+radval))

def entup():
    global entval
    entval = e1.get()
    update()

def btnup(a):
    global btnval
    btnval = a
    update()

def comup():
    global comval
    if str1 == 'High':
        comval = 100
    elif str1 == 'Mid':
        comval = 50
    elif str1 == 'Low':
        comval = 20
    else:
        comval = 0
    update()

"""def radup():"""



win=Tk()
win.title('main')
win.geometry('800x400')

ent=IntVar()
ent.set(0)
str1=StringVar()

label1 = Label(win,text="")

label1.pack()

e1 = Entry(win)
e1.bind("<Return>",entup)
inbtn = Button(win,text='input',command=entup())
e1.pack()
inbtn.pack()

a=['High', 'Mid', 'Low','0']
comb1 = atk.Combobox(win,values = a,textvariable=str1,state="readonly")
comb1.pack()

btn1 = Button(win,text='High',command=lambda i = 90:btnup(i))
btn2 = Button(win,text='Mid',command=lambda i = 40:btnup(i))
btn3 = Button(win,text='Low',command=lambda i = 0:btnup(i))

btn1.pack()
btn2.pack()
btn3.pack()

radio1 = Radiobutton()

win.mainloop()