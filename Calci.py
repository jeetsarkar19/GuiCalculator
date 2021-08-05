#Importing tkinter module
from tkinter import *
root = Tk()
root.title("Calculator")
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, padx=10, pady=10, columnspan = 3)

# Creating Buttons
def butadd(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)  + str(number))
def butclear():
    e.delete(0, END)
def butplus():
    current = e.get()
    global num
    global math
    math = "addition"
    num = int(current)
    e.delete(0, END)

def butminus():
    current = e.get()
    global num
    global math
    math = "subtraction"
    num = int(current)
    e.delete(0, END)
def butmul():
    current = e.get()
    global num
    global math
    math = "multiplication"
    num = int(current)
    e.delete(0, END)
def butdiv():
    current = e.get()
    global num
    global math
    math = "division"
    num = int(current)
    e.delete(0, END)
def butequal():
    current = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, num+int(current))
    elif math == "subtraction":
        e.insert(0, num - int(current))
    elif math == "multiplication":
        e.insert(0, num * int(current))
    elif math == "division":
        e.insert(0, num / int(current))

# Adding functionality to the button, eg clicking on 1 gives 1 and etc.
Button1 = Button(root, text="1", padx = 40, pady = 20,command = lambda: butadd(1))
Button2 = Button(root, text="2", padx = 40, pady = 20,command = lambda: butadd(2))
Button3 = Button(root, text="3", padx = 40, pady = 20,command = lambda: butadd(3))
Button4 = Button(root, text="4", padx = 40, pady = 20,command = lambda: butadd(4))
Button5 = Button(root, text="5", padx = 40, pady = 20,command = lambda: butadd(5))
Button6 = Button(root, text="6", padx = 40, pady = 20,command = lambda: butadd(6))
Button7 = Button(root, text="7", padx = 40, pady = 20,command = lambda: butadd(7))
Button8 = Button(root, text="8", padx = 40, pady = 20,command = lambda: butadd(8))
Button9 = Button(root, text="9", padx = 40, pady = 20,command = lambda: butadd(9))
Button0 = Button(root, text="0", padx = 40, pady = 20,command = lambda: butadd(0))
ButtonAdd = Button(root, text="+", padx = 39, pady = 20,command = lambda: butplus())
ButtonClear = Button(root, text="Clear", padx = 79, pady = 20,command = lambda: butclear())
ButtonEqual = Button(root, text="=", padx = 91, pady = 20,command = lambda: butequal())
ButtonMinus = Button(root, text="-", padx = 40, pady = 20,command = lambda: butminus())
ButtonMul = Button(root, text="*", padx = 40, pady = 20,command = lambda: butmul())
ButtonDiv = Button(root, text="/", padx = 41, pady = 20,command = lambda: butdiv())

# Placing the buttons on the screen using trial and error method
Button1.grid(row=3 , column=0 )
Button2.grid(row=3 , column=1 )
Button3.grid(row=3 , column=2 )
Button4.grid(row=2 , column=0 )
Button5.grid(row=2 , column=1 )
Button6.grid(row=2 , column=2 )
Button7.grid(row=1 , column=0 )
Button8.grid(row=1, column= 1)
Button9.grid(row=1 , column=2 )
Button0.grid(row=4 , column=0 )
ButtonClear.grid(row=4 , column=1, columnspan=2 )
ButtonAdd.grid(row=5 , column=0)
ButtonEqual.grid(row=5 , column=1, columnspan = 2 )
ButtonMinus.grid(row=6 , column=0)
ButtonMul.grid(row=6 , column=1)
ButtonDiv.grid(row=6 , column=2)
root.mainloop()
