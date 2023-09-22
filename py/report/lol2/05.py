from tkinter import *
import tkinter.ttk as atk


price = 0
menu = []

def menu_price(a):
    global price
    if a == 1:
        price +=10000
        menu.append('복어탕')
    elif a == 2:
        price +=10000
        menu.append('도루묵탕')
    elif a == 3:
        price +=10000
        menu.append('물메기탕')
    elif a == 4:
        price +=10000
        menu.append('장치조림')
    elif a == 5:
        price +=10000
        menu.append('대구탕')
    elif a == 6:
        price +=10000
        menu.append('문어볶음')
    elif a == 7:
        price +=13000
        menu.append('물곰국')

    str1.config(text=menu)
    str2.config(text=str(price))

def sum():
    money = e1.get()
    str3.config(text=str(int(money)-price))

win=Tk()
win.title('main')
win.geometry('800x400')

str1 = Label(win,text="")
str2 = Label(win,text="")

money=IntVar()
money.set(0)


str1.pack()
str2.pack()


btn1 = Button(win, text='복어탕 10000',command=lambda i = 1:menu_price(i))
btn2 = Button(win, text='도루묵탕 10000',command=lambda i = 2:menu_price(i))
btn3 = Button(win, text='물메기탕 10000',command=lambda i = 3:menu_price(i))
btn4 = Button(win, text='장치조림 10000',command=lambda i = 4:menu_price(i))
btn5 = Button(win, text='대구탕 10000',command=lambda i = 5:menu_price(i))
btn6 = Button(win, text='문어볶음 10000',command=lambda i = 6:menu_price(i))
btn7 = Button(win, text='물곰국 13000',command=lambda i = 7:menu_price(i))

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()

e1 = Entry(win)
e1.pack()
btna = Button(win, text='계산',command=sum)

btna.pack()
str3 = Label(win,text="")
str3.pack()
win.mainloop()