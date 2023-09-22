from tkinter import *
import tkinter.ttk as atk

def update():
    l1.config(text = str(eti.get() + bti.get() + cbi.get() + rdi.get()))

def entry():
    eti.set(int(e1.get()))
    update()

def bt(a):
    bti.set(a)
    update()

def com():
    str1 = combox1.get()
    if str1 == 'High':
        cbi.set(100)
    elif str1 == 'Mid':
        cbi.set(50)
    elif str1 == 'Low':
        cbi.set(20)
    else:
        cbi.set(0)
    update()

def rad():
    n = radval.get()
    rdi.set(n)
    update()

win = Tk()
win.title('main')
win.geometry('800x400')

eti = IntVar()
eti.set(0)
bti = IntVar()
bti.set(0)
cbi = IntVar()
cbi.set(0)
rdi = IntVar()
rdi.set(0)
str1 = StringVar()

l1 = Label(win, text = '0')
l1.pack()

e1 = Entry(win)
e1.pack()

btinput = Button(win, text = 'input', command = entry)
btinput.pack()

combox1 = atk.Combobox(win, state = 'readonly')
combox1['values'] = ('High','Mid','Low','0')
combox1.current(3)
combox1.pack()
cb = Button(win, text = 'comin', command = com)
cb.pack()

b1 = Button(win, text = 'High',command = lambda p1 = 90 : bt(p1))
b2 = Button(win, text = 'mid',command = lambda p1= 40 : bt(p1))
b3 = Button(win, text = 'Low',command = lambda p1 = 0 : bt(p1))


b1.pack()
b2.pack()
b3.pack()

radval = IntVar()

r1 = Radiobutton(win, text = 'High', variable = radval, value = 80, command=rad)
r2 = Radiobutton(win, text = 'Mid', variable = radval, value = 35, command=rad)
r3 = Radiobutton(win, text = 'Low', variable = radval, value = 10, command=rad)
r4 = Radiobutton(win, text = '0', variable = radval, value = 0, command=rad)

r1.pack()
r2.pack()
r3.pack()
r4.pack()

win.mainloop()