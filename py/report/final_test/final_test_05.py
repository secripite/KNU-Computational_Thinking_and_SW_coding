from tkinter import *
import tkinter.ttk as atk

resert = ''

def update():
    global resert
    reser.config(text=resert)

def plus():
    global resert
    resert = str(int(ent1.get()) + int(ent2.get()))
    update()

def minus():
    global resert
    resert = str(int(ent1.get()) - int(ent2.get()))
    update()

def times():
    global resert
    resert = str(int(ent1.get()) * int(ent2.get()))
    update()

def divide():
    global resert
    resert = str(int(ent1.get()) // int(ent2.get()))
    update()

win = Tk()
win.title('main')
win.geometry('800x400')

Oprand1 = Label(win, text='Oprand1')
Oprand2 = Label(win, text='Oprand2')

ent1 = Entry(win)
ent2 = Entry(win)

Oprand1.pack()
ent1.pack()
Oprand2.pack()
ent2.pack()

plbtn = Button(win, text='+', command=plus)
mibtn = Button(win, text='-', command=minus)
tibtn = Button(win, text='*', command=times)
dibtn = Button(win, text='/', command=divide)

plbtn.pack()
mibtn.pack()
tibtn.pack()
dibtn.pack()

reser = Label(win, text='')
res = Label(win, text='Result')
res.pack()
reser.pack()

win.mainloop()