from tkinter import *
from unittest import result

root = Tk()
root.title("Calculator")
root.geometry("300x200")

min_width = 300
min_height = 230
root.minsize(min_width, min_height)

# Functions

operation = "arithmetic"

def switch(): # Changing Operation
    global operation

    if operation == "arithmetic":
        operation = "geometric"
    else:
        operation = "arithmetic"
    
def calculate(): # Calculation
    if entry1.get() == '' or entry2.get() == '' or entry3.get() == '':
        calculation.config(text="Error, please input a number in all fields")
    elif operation == "arithmetic":
        total = 0
        for i in range(int(entry3.get())):
            if int(entry3.get()) >= 0:
                calculation.config(text="Error, do not input 0")
            total += (int(entry3.get()) / 2) * (2 * int(entry1.get())) + int(entry3.get()) - 1 * int(entry2.get())
        calculation.config(text="Arithmetic series is: " + str(total))
    else:
        total = 0
        for i in range(int(entry3.get())):
            total += int(entry1.get()) ** int(entry2.get())
        calculation.config(text="Geometric series is: " + str(total))

# font size changer
def small():
    entry1.place(x=130, y=10)
    entry2.place(x=130, y=50)
    entry3.place(x=130, y=90)
    labelA.place(x=10, y=15)
    labelB.place(x=10, y=55)
    labelC.place(x=10, y=95)
    button1.place(x=10, y=130)
    button2.place(x=70, y=130)
    calculation.place(x=10, y=160)
    clear.place(x=10, y=190)

    labelA.config(font=('Arial', 9))
    labelB.config(font=('Arial', 9))
    labelC.config(font=('Arial', 9))
    entry1.config(font=('Arial', 18))
    entry2.config(font=('Arial', 18))
    entry3.config(font=('Arial', 18))
    button1.config(font=('Arial', 9))
    button2.config(font=('Arial', 9))
    calculation.config(font=('Arial', 9))
    clear.config(font=('Arial', 9))
    root.geometry("300x200")
    
def medium():
    entry1.place(x=300, y=15)
    entry2.place(x=300, y=70)
    entry3.place(x=300, y=125)
    labelA.place(x=10, y=20)
    labelB.place(x=10, y=75)
    labelC.place(x=10, y=130)
    button1.place(x=10, y=200)
    button2.place(x=130, y=200)
    calculation.place(x=10, y=250)
    clear.place(x=10, y=350)

    labelA.config(font=('Arial', 22))
    labelB.config(font=('Arial', 22))
    labelC.config(font=('Arial', 22))
    entry1.config(font=('Arial', 25))
    entry2.config(font=('Arial', 25))
    entry3.config(font=('Arial', 25))
    button1.config(font=('Arial', 22))
    button2.config(font=('Arial', 22))
    calculation.config(font=('Arial', 15))
    clear.config(font=('Arial', 15))
    root.geometry("500x400")

def large():
    entry1.place(x=450, y=15)
    entry2.place(x=450, y=75)
    entry3.place(x=450, y=135)
    labelA.place(x=10, y=20)
    labelB.place(x=10, y=80)
    labelC.place(x=10, y=140)
    button1.place(x=10, y=225)
    button2.place(x=200, y=225)
    calculation.place(x=10, y=350)
    clear.place(x=10, y=510)

    labelA.config(font=('Arial', 28))
    labelB.config(font=('Arial', 28))
    labelC.config(font=('Arial', 28))
    entry1.config(font=('Arial', 28))
    entry2.config(font=('Arial', 28))
    entry3.config(font=('Arial', 28))
    button1.config(font=('Arial', 28))
    button2.config(font=('Arial', 28))
    calculation.config(font=('Arial', 28))
    clear.config(font=('Arial', 28))
    root.geometry("700x600")

# Create labels
global labelA
labelA = Label(root, text="Num Entry", font=("Arial", 9))
labelA.place(x=10, y=15)

global labelB
labelB = Label(root, text="Common Difference", font=("Arial", 9))
labelB.place(x=10, y=55)

global labelC
labelC = Label(root, text="Num of Terms", font=("Arial", 9))
labelC.place(x=10, y=95)

# Theming

theme = "light"

def switchtheme():
    global theme

    if theme == "light":
        darkmode()
        theme = "dark"
    else:
        lightmode()
        theme = "light"

def darkmode(): # Dark Theme
    root.config(bg="#1f1f1f")

    for themed in root.winfo_children():
        if isinstance(themed, Entry):
            themed.config(bg="#2a2a2a", fg="#ffffff")
        elif isinstance(themed, Button):
            themed.config(bg="#363636", fg="#ffffff")
        elif isinstance(themed, Radiobutton):
            themed.config(bg="#1F1F1F", fg="#ffffff")
        elif isinstance(themed, Label):
            themed.config(bg="#1F1F1F", fg="#ffffff")
    calculation.config(fg="#ffffff")

def lightmode(): # Light Theme
    root.config(bg="#f0f0f0")

    for themed in root.winfo_children():
        if isinstance(themed, Entry):
            themed.config(bg="#ffffff", fg="#000000")
        elif isinstance(themed, Button):
            themed.config(bg="#eeeeee", fg="#000000")
        elif isinstance(themed, Radiobutton):
            themed.config(bg="#f0f0f0", fg="#000000")
        elif isinstance(themed, Label):
            themed.config(bg="#f0f0f0", fg="#000000")
    calculation.config(fg="#000000")

# Translator
def translation():
    "hi"


# Create Entry Widget Input Box

global entry1
entry1 = Entry(root, width=10, font=("Arial", 18))
entry1.place(x=130, y=10)

global entry2
entry2 = Entry(root, width=10, font=("Arial", 18))
entry2.place(x=130, y=50)

global entry3
entry3 = Entry(root, width=10, font=("Arial", 18))
entry3.place(x=130, y=90)

# Create Buttons
global button1
var = IntVar()
button1 = Radiobutton(root, text="Switch Operation", command=switch, variable = var, value = 1, font=("Arial", 9))
button1.place(x=10, y=130)

global button2
button2 = Radiobutton(root, text="Calculate", command=calculate, variable = var, value = 2, font=("Arial", 9))
button2.place(x=70, y=130)

global calculation
calculation = Label(root, text="", font=("Arial", 9))
calculation.place(x=10, y=160)

global clear
clear = Button(root, width=5, text="Clear", command=lambda: calculation.config(text=""), font=("Arial", 9))
clear.place(x=10, y=190)

# Create File toolbar

menubar = Menu(root)
root.config(menu=menubar)

menufile = Menu(menubar, tearoff=0)
menufont = Menu(menubar, tearoff=0)
menutran = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=menufile)
menubar.add_cascade(label="Change Font Size", menu=menufont)
menubar.add_cascade(label="Translate", menu=menutran)

menufile.add_command(label="Switch Theme", command=switchtheme)
menufile.add_separator()
menufile.add_command(label="Exit", command=root.destroy)

menufont.add_command(label="small", command=small)
menufont.add_command(label="medium", command=medium)
menufont.add_command(label="large", command=large)

menutran.add_command(label="English")
menutran.add_command(label="French")

root.mainloop()