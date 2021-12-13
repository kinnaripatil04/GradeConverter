from tkinter import *

root = Tk()
root.title(" Grade Converter")

e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=1, columnspan=4, padx=10, pady=10)


def button_click(a):
    #e.delete(0,END)
    current= e.get()
    e.delete(0, END)
    e.insert(0,str(current) +str(a))

def button_clear():
    e.delete(0, END)

def button_equal():
    b = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(b))
    if math=="subtraction":
        e.insert(0, f_num - float(b))
    if math=="division":
        e.insert(0, f_num / float(b))
    if math=="multiplication":
        e.insert(0, f_num * float(b))
    if math=="exponential":
        e.insert(0,f_num ** float(b))
    if math=="modulus":
        e.insert(0,f_num % float(b))




def button_add():
    a=e.get()
    global f_num
    global math
    math="addition"
    f_num=float(a)
    e.delete(0, END)

def button_sub():
    a = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(a)
    e.delete(0, END)

def button_div():
    a = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(a)
    e.delete(0, END)

def button_mul():
    a = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(a)
    e.delete(0, END)


def button_exp():
    a = e.get()
    global f_num
    global math
    math = "exponential"
    f_num = float(a)
    e.delete(0, END)

def button_per():
    a = e.get()
    global f_num
    f_num = float(a)
    if(f_num < 7):
        b = 7.1 * f_num + 12
        e.insert(0, b)
    else:
        b = 7.4 * f_num + 12
        e.insert(0, b)

def button_modulus():
    a = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = float(a)
    e.delete(0, END)




# define the buttons

button_1 = Button(root, text="1", padx=40, pady=20, fg="black", bg="rosy brown", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, fg="black", bg="rosy brown", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, fg="black", bg="rosy brown", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, fg="black", bg="rosy brown", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, fg="black", bg="rosy brown", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, fg="black", bg="rosy brown", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, fg="black", bg="rosy brown", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, fg="black", bg="rosy brown", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, fg="black", bg="rosy brown", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, fg="black", bg="rosy brown", command=lambda: button_click(0))
button_equal = Button(root, text="=", padx=40, pady=20, fg="black", bg="azure", command=button_equal)
button_add = Button(root, text="+", padx=40, pady=20, fg="black", bg="AntiqueWhite3", command=button_add)
button_sub = Button(root, text="-", padx=40, pady=20, fg="black", bg="AntiqueWhite3", command=button_sub)
button_div = Button(root, text="/", padx=40, pady=20, fg="black", bg="AntiqueWhite3", command=button_div)
button_mul = Button(root, text="*", padx=40, pady=20, fg="black", bg="AntiqueWhite3", command=button_mul)
button_point = Button(root, text=".", padx=42, pady=20, fg="black", bg="AntiqueWhite3", command=lambda: button_click("."))
button_cgpa = Button(root, text="m", padx=40, pady=20, fg="black", bg="AntiqueWhite3", command=button_modulus)
button_per = Button(root, text="%", padx=40, pady=20, fg="black", bg="AntiqueWhite3", command=button_per)
button_exp = Button(root, text="^", padx=40, pady=20, fg="black", bg="AntiqueWhite3", command=button_exp)
button_clear = Button(root, text="C", padx=40, pady=20, fg="black", bg="lavender blush2", command=button_clear)

# put the buttons on the screen

button_clear.grid(row=5, column=1)
button_0.grid(row=5, column=2)
button_equal.grid(row=5, column=3)
button_point.grid(row=5,column=4)

button_1.grid(row=4, column=1)
button_2.grid(row=4, column=2)
button_3.grid(row=4, column=3)
button_per.grid(row=4,column=4)

button_4.grid(row=3, column=1)
button_5.grid(row=3, column=2)
button_6.grid(row=3, column=3)
button_cgpa.grid(row=3,column=4)

button_7.grid(row=2, column=1)
button_8.grid(row=2, column=2)
button_9.grid(row=2, column=3)
button_sub.grid(row=2,column=4)

button_exp.grid(row=1,column=1)
button_div.grid(row=1,column=2)
button_mul.grid(row=1,column=3)
button_add.grid(row=1,column=4)




root.mainloop()
