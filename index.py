from tkinter import *
from tkinter import font
from customtkinter import *

root = CTk()
root.title("Calculator")
root.geometry("350x440")

default_font = font.nametofont("TkDefaultFont")  # Get default font value into Font object
print(default_font.actual())

min_width = 200
min_height = 250
root.minsize(min_width, min_height)
set_widget_scaling(1.8)

# Functions

operation = "arithmetic"

def switch(selection): # Changing Operation
    global operation
    operation = selection.casefold()
    
def calculate(): # Calculation
    if entry1.get() == '' or entry2.get() == '' or entry3.get() == '':
        calculation.configure(text="Error: Input a number in all fields!")
    elif operation == "arithmetic":
        total = 0
        for i in range(int(entry3.get())):
            if int(entry3.get()) >= 0:
                calculation.configure(text="Error, Do not input 0!")
            total += (int(entry3.get()) / 2) * (2 * int(entry1.get())) + int(entry3.get()) - 1 * int(entry2.get())
        calculation.configure(text="Arithmetic series is: " + str(total))
    else:
        total = 0
        for i in range(int(entry3.get())):
            total += int(entry1.get()) ** int(entry2.get())
        calculation.configure(text="Geometric series is: " + str(total))

# Sizing

def small():
    root.geometry("200x250")
    set_widget_scaling(1.0)
    
def medium():
    root.geometry("350x440")
    set_widget_scaling(1.8)

def large():
    root.geometry("490x620")
    set_widget_scaling(2.5)

# Create labels

global numLabel
numLabel = CTkLabel(root, text="Num Entry", font=("Arial", 10))
numLabel.place(x=10, y=10)

global diffLabel
diffLabel = CTkLabel(root, text="Common Difference", font=("Arial", 10))
diffLabel.place(x=10, y=50)

global termsLabel
termsLabel = CTkLabel(root, text="Num of Terms", font=("Arial", 10))
termsLabel.place(x=10, y=90)

global calculation
calculation = CTkLabel(root, text="", font=("Arial", 10))
calculation.place(x=10, y=210)

# Translator

def translation():
    "hi"

# Create Entry Widget Input Box

global entry1
entry1 = CTkEntry(root, width=70, font=("Arial", 10))
entry1.place(x=110, y=10)

global entry2
entry2 = CTkEntry(root, width=70, font=("Arial", 10))
entry2.place(x=110, y=50)

global entry3
entry3 = CTkEntry(root, width=70, font=("Arial", 10))
entry3.place(x=110, y=90)

# Create Buttons

global switchButton
var = IntVar()
switchButton = CTkSegmentedButton(root, values=["Arithmetic", "Geometric"], variable=var, command=switch, font=("Arial", 10))
switchButton.place(x=10, y=130)
switchButton.set("Arithmetic")

global calcButton
calcButton = CTkButton(root, width=170, text="Calculate", command=calculate, font=("Arial", 10))
calcButton.place(x=10, y=170)

global clear
clear = CTkButton(root, width=40, text="Clear", command=lambda: calculation.configure(text=""), font=("Arial", 10))
clear.place(x=140, y=130)

# Create File toolbar

menubar = Menu(root)
root.configure(menu=menubar)

menufile = Menu(menubar, tearoff=0)
menuthem = Menu(menubar, tearoff=0)
menufont = Menu(menubar, tearoff=0)
menutran = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=menufile)
menubar.add_cascade(label="Theme", menu=menuthem)
menubar.add_cascade(label="Sizing", menu=menufont)
menubar.add_cascade(label="Translate", menu=menutran)

menufile.add_command(label="About")
menufile.add_separator()
menufile.add_command(label="Exit", command=root.destroy)

menuthem.add_cascade(label="Dark", command=lambda: set_appearance_mode("dark"))
menuthem.add_cascade(label="Light", command=lambda: set_appearance_mode("light"))

menufont.add_command(label="Small", command=small)
menufont.add_command(label="Medium", command=medium)
menufont.add_command(label="Large", command=large)

menutran.add_command(label="English")
menutran.add_command(label="French")

root.mainloop()