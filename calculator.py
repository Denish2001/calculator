from tkinter import*
root=Tk()
root.title("simple calculator")

e=Entry(root,width=45,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

def button_click(number):

    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0, END)
def button_add():
    firstnumber=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(firstnumber)
    e.delete(0,END)

def button_subtract():
    firstnumber = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(firstnumber)
    e.delete(0, END)


def button_divide():
    firstnumber = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(firstnumber)
    e.delete(0, END)
def button_multiply():
    firstnumber = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(firstnumber)
    e.delete(0, END)
def button_equal():
    second_number=e.get()
    e.delete(0, END)

    if math=="addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math=="multiplication":
        e.insert(0, f_num * int(second_number))
    if math=="division":
        e.insert(0, f_num / int(second_number))


b1=Button(root,text=1,width=15,height=5,command=lambda: button_click(1))
b1.grid(row=1,column=0)

b2=Button(root,text=2,width=15,height=5,command=lambda: button_click(2))
b2.grid(row=1,column=1)

b3=Button(root,text=3,width=15,height=5,command=lambda: button_click(3))
b3.grid(row=1,column=2)

b4=Button(root,text=4,width=15,height=5,command=lambda: button_click(4))
b4.grid(row=2,column=0)

b5=Button(root,text=5,width=15,height=5,command=lambda: button_click(5))
b5.grid(row=2,column=1)

b6=Button(root,text=6,width=15,height=5,command=lambda: button_click(6))
b6.grid(row=2,column=2)

b7=Button(root,text=7,width=15,height=5,command=lambda: button_click(7))
b7.grid(row=3,column=0)

b8=Button(root,text=8,width=15,height=5,command=lambda: button_click(8))
b8.grid(row=3,column=1)

b9=Button(root,text=9,width=15,height=5,command=lambda: button_click(9))
b9.grid(row=3,column=2)

b0=Button(root,text=0,width=15,height=5,command=lambda: button_click(0))
b0.grid(row=4,column=0)

bclear=Button(root,text="clear",width=30,height=5,command= button_clear)
bclear.grid(row=4,column=1,columnspan=2)

badd=Button(root,text="+",width=15,height=5,command= button_add)
badd.grid(row=5,column=0)

bequal=Button(root,text="=",width=30,height=5,command= button_equal)
bequal.grid(row=5,column=1,columnspan=2)

bsubtract=Button(root,text="-",width=15,height=5,command= button_subtract)
bsubtract.grid(row=6,column=0)

bdivide=Button(root,text="/",width=15,height=5,command= button_divide)
bdivide.grid(row=6,column=1)

bmultiply=Button(root,text="*",width=15,height=5,command= button_multiply)
bmultiply.grid(row=6,column=2)

root.mainloop()
