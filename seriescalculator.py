from tkinter import *
from tkinter import font
from tkinter import messagebox
from customtkinter import *

root = CTk()
root.title("Calculator")
root.geometry("345x470")
root.minsize(345, 470)
set_widget_scaling(1.8)

default_font = font.nametofont("TkDefaultFont")  # Get default font value into Font object
print(default_font.actual())

# Functions

operation = StringVar()

def switch(selection): # Changing Operation
    global operation
    operation.set(selection)
    
def calculate(): # Calculation
    try:
        i=0
        # replacing entry boxes as one lettered variables to simplify code
        f = float(entry1.get())
        c = float(entry2.get())
        n = int(entry3.get())

        if n <= 0:
            calculation.configure(text="Error: Input values above 0!")
        elif n > 999999:
            calculation.configure(text="Error: Integer overflow, input less")
        else:
            opVal = operation.get()
            # Arithmetic series calculation
            if opVal == "Arithmetic":
                total = f
                while i in range(n-1):
                    f=f+c
                    total=total+f
                    i += 1
                calculation.configure(text="Arithmetic series is: " + "\n" + str(total))
            elif opVal == "Geometric":
                # Geometric series calculation
                total = f
                while i in range(n-1):
                    f=f*c
                    total=total+f
                    i += 1
                calculation.configure(text="Geometric series is: " + "\n" + str(total))
    except ValueError:
        calculation.configure(text="Error: Input only numbers")
    except OverflowError:
        calculation.configure(text="Error: Integer overflow, input less")

# Sizing

def small():
    set_widget_scaling(1.0)
    root.minsize(190, 260)
    root.geometry("190x260")
    
def medium():
    set_widget_scaling(1.8)
    root.minsize(345, 470)
    root.geometry("345x470")

def large():
    set_widget_scaling(2.4)
    root.minsize(470, 630)
    root.geometry("470x630")

# About popup

def about():
    messagebox.showinfo("About", "A Summing Series calculator. \n By Sahaj & Ethan \n\n https://github.com/EthanSDD/SummingSeries \n Licensed under GPL-3.0")

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
calculation.place(x=10, y=225)

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

arithmeticButton = CTkRadioButton(root, text="Arithmetic", variable=operation, value="Arithmetic", command=lambda: switch("Arithmetic"), font=("Arial", 10))
arithmeticButton.place(x=10, y=130)

geometricButton = CTkRadioButton(root, text="Geometric", variable=operation, value="Geometric" ,command=lambda: switch("Geometric"), font=("Arial", 10))
geometricButton.place(x=10, y=160)

calcButton = CTkButton(root, width=170, text="Calculate", command=calculate, font=("Arial", 10))
calcButton.place(x=10, y=190)

clear = CTkButton(root, width=80, text="Clear", command=lambda: calculation.configure(text=""), font=("Arial", 10))
clear.place(x=100, y=140)

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

menufile.add_command(label="About", command=about)
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