from tkinter import *

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

    if operation == "arithmetic":
        result = int(entry1.get()) + int(entry2.get())
        calculation.config(text="Arithmetic series is: " + str(result))
    else:
        result = int(entry1.get()) * int(entry2.get())
        calculation.config(text="Geometric series is: " + str(result))

# Create labels

labelA = Label(root, text="Num Entry")
labelA.place(x=10, y=15)

labelB = Label(root, text="Common Difference")
labelB.place(x=10, y=55)

labelC = Label(root, text="Num of Terms")
labelC.place(x=10, y=95)

# Create Entry Widget Input Box

entry1 = Entry(root, width=10, font=("Helvetica", 18))
entry1.place(x=130, y=10)

entry2 = Entry(root, width=10, font=("Helvetica", 18))
entry2.place(x=130, y=50)

entry3 = Entry(root, width=10, font=("Helvetica", 18))
entry3.place(x=130, y=90)

# Create Buttons

button1 = Radiobutton(root, text="Switch Operation", command=switch)
button1.place(x=10, y=130)

button2 = Radiobutton(root, text="Calculate", command=calculate)
button2.place(x=70, y=130)

calculation = Label(root, text="")
calculation.place(x=10, y=160)

clear = Button(root, width=5, text="Clear", command=lambda: calculation.config(text=""))
clear.place(x=10, y=190)

root.mainloop()