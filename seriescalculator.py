from tkinter import *
from tkinter import messagebox
from customtkinter import *
from googletrans import *
from googletrans import Translator, LANGUAGES

root = CTk()
root.title("Calculator")
root.geometry("345x470")
root.minsize(345, 470)
set_widget_scaling(1.8)

# Functions

operation = StringVar()

def switch(selection): # Changing Operation
    global operation
    operation.set(selection)

calcErrors = ["Error:", "Input values above 0!", "Integer overflow, input less", "Input only numbers"]
sumDisplay = ["{} series is:", "Arithmetic", "Geometric"]    
def calculate(): # Calculation
    try:
        i=0
        # replacing entry boxes as one lettered variables to simplify code
        f = float(entry1.get())
        c = float(entry2.get())
        n = int(entry3.get())

        if n <= 0:
            calculation.configure(text=f"{calcErrors[0]} {calcErrors[1]}")
        elif n > 999999:
            calculation.configure(text=f"{calcErrors[0]} {calcErrors[2]}")
        else:
            opVal = operation.get()
            # Arithmetic series calculation
            if opVal == "Arithmetic":
                total = f
                while i in range(n-1):
                    f=f+c
                    total=total+f
                    i += 1
                calculation.configure(text=f"{sumDisplay[0].format(sumDisplay[1])}\n{str(total)}")
            elif opVal == "Geometric":
                # Geometric series calculation
                total = f
                while i in range(n-1):
                    f=f*c
                    total=total+f
                    i += 1
                calculation.configure(text=f"{sumDisplay[0].format(sumDisplay[2])}\n{str(total)}")
    except ValueError:
        calculation.configure(text=f"{calcErrors[0]} {calcErrors[3]}")
    except OverflowError:
        calculation.configure(text=f"{calcErrors[0]} {calcErrors[2]}")

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
    messagebox.showinfo(transDict["aboutMessageBox"][0], 
                    f"{transDict['aboutMessageBox'][1]} \n By Sahaj & Ethan \n\n \
                    https://github.com/EthanSDD/SummingSeries \n \
                    {transDict['aboutMessageBox'][2].format('GPL-3.0')}")

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

transDict = { # Translated text
    "labels" : ["Num Entry", "Common Difference", "Num of Terms"],
    "buttons" : ["Clear", "Calculate"],
    "radiobuttons" : ["Arithmetic", "Geometric"],
    "title" : ["Calculator"],
    "filemenu" : ["File", "Theme", "Sizing", "Translate", "About", "Exit", "Dark", "Light",
                   "Small", "Medium", "Large"],
    "sameLang" : ["You cannot change the program to the same language"],
    "aboutMessageBox" : ["About", "A Summing Series calculator.", "Licensed under {}"],
    "errors" : ["Error:", "Input values above 0!", "Integer overflow, input less", "Input only numbers"],  
    "sum" : ["{} series is:", "Arithmetic", "Geometric"]
}

english = transDict.copy()
translator = Translator()
sameLang = "Cannot change to the same language"
currentLang = "english"

def translate(language):
    global english
    global transDict
    global sameLang
    global currentLang
    global dictBefore
    global calcErrors
    global sumDisplay

    dictBefore = transDict.copy()

    if language == currentLang:
        messagebox.showerror(transDict["errors"][0], sameLang)
        return
    
    currentLang = language

    if language != "en":
        for key in transDict:
            transDict[key] = [translator.translate(text, dest = language, src = "en").text for text in transDict[key]]
    else:
        transDict = english
    
    numLabel.configure(text = transDict["labels"][0])
    diffLabel.configure(text = transDict["labels"][1])
    termsLabel.configure(text = transDict["labels"][2])
    clear.configure(text = transDict["buttons"][0])
    calcButton.configure(text = transDict["buttons"][1])
    arithmeticButton.configure(text = transDict["radiobuttons"][0])
    geometricButton.configure(text = transDict["radiobuttons"][1])

    root.title(transDict["title"][0])

    menubar.entryconfigure(dictBefore["filemenu"][0], label = transDict["filemenu"][0])
    menubar.entryconfigure(dictBefore["filemenu"][1], label = transDict["filemenu"][1])
    menubar.entryconfigure(dictBefore["filemenu"][2], label = transDict["filemenu"][2])
    menubar.entryconfigure(dictBefore["filemenu"][3], label = transDict["filemenu"][3])
    
    menufile.entryconfigure(dictBefore["filemenu"][4], label = transDict["filemenu"][4])
    menufile.entryconfigure(dictBefore["filemenu"][5], label = transDict["filemenu"][5])
    
    menuthem.entryconfigure(dictBefore["filemenu"][6], label = transDict["filemenu"][6])
    menuthem.entryconfigure(dictBefore["filemenu"][7], label = transDict["filemenu"][7])
    
    menufont.entryconfigure(dictBefore["filemenu"][8], label = transDict["filemenu"][8])
    menufont.entryconfigure(dictBefore["filemenu"][9], label = transDict["filemenu"][9])
    menufont.entryconfigure(dictBefore["filemenu"][10], label = transDict["filemenu"][10])

    sameLang = transDict["sameLang"][0]
    calcErrors = transDict["errors"]
    sumDisplay = transDict["sum"]

    calculate()
    dictBefore = transDict

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

languages = LANGUAGES
for acronym, langName in languages.items():
    menutran.add_command(label = langName, command = lambda _ = acronym: translate(_))

root.mainloop()