import tkinter
from tkinter import *
from tkinter import messagebox
import time
import random

#window formatiing
root=Tk()
root.title("RESTURANT MANAGEMENT SYSTEM")
root.geometry("675x275")
root.resizable(True,True)

oreder_no = StringVar()
fl = StringVar()
ll = StringVar()
bl = StringVar()
pl = StringVar()
cl = StringVar()
dl = StringVar()
col = StringVar()
scl = StringVar()
tl = StringVar()
sl = StringVar()
ttl = StringVar()

def create():
    sub = Toplevel(root)
    sub.title("Sub Window")
    sub.geometry("205x160+800+145")

    label1=Label(sub,text='ITEM',width=10,font=50,fg='red',bg="pink")
    label1.grid(row=0,column=0)
    label1 = Label(sub, text='PRICE', width=10, font=50,fg='red',bg="pink")
    label1.grid(row=0, column=1)

    label1 = Label(sub, text='FRIES MEAL', fg='blue')
    label1.grid(row=1, column=0)
    label1=Label(sub,text='50',fg='blue')
    label1.grid(row=1,column=1)
    label1 = Label(sub, text='LUNCH', fg='blue')
    label1.grid(row=2, column=0)
    label1=Label(sub,text='100',fg='blue')
    label1.grid(row=2,column=1)
    label1 = Label(sub, text='BURGER MEAL', fg='blue')
    label1.grid(row=3, column=0)
    label1=Label(sub,text='25',fg='blue')
    label1.grid(row=3,column=1)
    label1 = Label(sub, text='PIZZA MEAL', fg='blue')
    label1.grid(row=4, column=0)
    label1=Label(sub,text='50',fg='blue')
    label1.grid(row=4,column=1)
    label1 = Label(sub, text='CHEESE BURGER', fg='blue')
    label1.grid(row=5, column=0)
    label1=Label(sub,text='45',fg='blue')
    label1.grid(row=5,column=1)
    label1 = Label(sub, text='DRINK', fg='blue')
    label1.grid(row=6, column=0)
    label1=Label(sub,text='30',fg='blue')
    label1.grid(row=6,column=1)
def total():
    global total
    a=int(entry2.get())
    b=int(entry3.get())
    c=int(entry5.get())
    d=int(entry7.get())
    e=int(entry9.get())
    f=int(entry11.get())
    g=random.randrange(2299,8000)
    total=int(30*a+50*b+100*c+25*d+50*e+45*f)
    tax1=(total*9)/100
    service1=(total*3)/100
    total1=total+tax1+service1
    col.set(total)
    scl.set(service1)
    tl.set(tax1)
    sl.set(total)
    ttl.set(total1)

def reset():
    oreder_no.set('')
    fl.set('')
    ll.set('')
    bl.set('')
    pl.set('')
    cl.set('')
    dl.set('')
    col.set('')
    scl.set('')
    tl.set('')
    sl.set('')
    ttl.set('')


def exit():
    result=messagebox.askyesno("Alert","do you want to exit")
    if result==True:
        sys.exit()
    else:
        pass




frame2=Frame(root)
frame2.pack(side=TOP)

label=Label(frame2,text="Resturant Management System",font=1000,fg="blue",height=3)
label.pack()

frame=Frame(root)
frame.pack(side=TOP)

label1=Label(frame,text="Order no.",width=10,font=20,fg="blue")
label1.grid(row=0,column=0)
list6=Entry(frame,width=20,bg="light blue",justify='right',textvariable=oreder_no)
list6.grid(row=0,column=1)

label2=Label(frame,text="Drink",width=10,font=20,fg="blue")
label2.grid(row=0,column=2)
entry2=Entry(frame,width=20,bg="light blue",justify='right', textvariable=dl)
entry2.grid(row=0,column=3)
#
label3=Label(frame,text="Fries Meal",width=10,font=20,fg="blue")
label3.grid(row=1,column=0)
entry3=Entry(frame,width=20,bg="light blue",justify='right', textvariable=fl)
entry3.grid(row=1,column=1)

label4=Label(frame,text="cost",width=10,font=20,fg="blue")
label4.grid(row=1,column=2)
list1=Entry(frame,width=20,bg="light blue",justify='right',textvariable=col)
list1.grid(row=1,column=3)

label5=Label(frame,text="Lunch",width=10,font=20,fg="blue")
label5.grid(row=2,column=0)
entry5=Entry(frame,width=20,bg="light blue",justify='right',textvariable=ll)
entry5.grid(row=2,column=1)

label6=Label(frame,text="Service Charge",width=20,font=20,fg="blue")
label6.grid(row=2,column=2)
list2=Entry(frame,width=20,bg="light blue",justify='right',textvariable=scl)
list2.grid(row=2,column=3)

label7=Label(frame,text="Burger Meal",width=10,font=20,fg="blue")
label7.grid(row=3,column=0)
entry7=Entry(frame,width=20,bg="light blue",justify='right',textvariable=bl)
entry7.grid(row=3,column=1)

label8=Label(frame,text="Tax",width=10,font=20,fg="blue")
label8.grid(row=3,column=2)
list3=Entry(frame,width=20,bg="light blue",justify='right', textvariable=tl)
list3.grid(row=3,column=3)

label9=Label(frame,text="Pizza Meal",width=10,font=20,fg="blue")
label9.grid(row=4,column=0)
entry9=Entry(frame,width=20,bg="light blue",justify='right',textvariable=pl)
entry9.grid(row=4,column=1)

label10=Label(frame,text="Subtotal",width=10,font=20,fg="blue")
label10.grid(row=4,column=2)
list4=Entry(frame,width=20,bg="light blue",justify='right',textvariable=sl)
list4.grid(row=4,column=3)

label11=Label(frame,text="Cheese burger",width=20,font=20,fg="blue")
label11.grid(row=5,column=0)
entry11=Entry(frame,width=20,bg="light blue",justify='right',textvariable=cl)
entry11.grid(row=5,column=1)

label12=Label(frame,text="Total",width=10,font=20,fg="blue")
label12.grid(row=5,column=2)
list5=Entry(frame,width=20,bg="light blue",justify='right', textvariable=ttl)
list5.grid(row=5,column=3)

frame3=Frame(root,bg="green")
frame3.pack(side=TOP)

b1=Button(frame3,text='PRICE',font=40,bg='light blue',width=10,height=1,command=create)
b1.pack(side=LEFT)

b2=Button(frame3,text='TOTAL',font=40,bg='light blue',width=10,height=1,command=total)
b2.pack(side=LEFT)

b1=Button(frame3,text='RESET',font=40,bg='light blue',width=10,height=1,command=reset)
b1.pack(side=LEFT)

b1=Button(frame3,text='EXIT',font=40,bg='light blue',width=10,height=1,command=exit)
b1.pack(side=LEFT)

g=random.randrange(2299,8000)
list6.insert(END,g)

root.mainloop()

