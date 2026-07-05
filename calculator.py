from tkinter import *
from tkinter import messagebox
import math

# WINDOW 
root = Tk()
root.title("Mathematical Calculator")
root.geometry("500x700")
root.resizable(False, False)

expression = ""

# DISPLAY 
entry = Entry(root,
              font=("Arial", 24),
              bd=8,
              relief=RIDGE,
              justify="right")
entry.pack(fill=X, padx=10, pady=10, ipady=15)

# FUNCTIONS 
def press(value):
    global expression
    expression += str(value)
    entry.delete(0, END)
    entry.insert(END, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, END)

def delete():
    global expression
    expression = expression[:-1]
    entry.delete(0, END)
    entry.insert(END, expression)

def equal():
    global expression
    try:
        exp = expression.replace("^", "**")
        result = str(eval(exp))
        entry.delete(0, END)
        entry.insert(END, result)
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Expression")
        clear()

def square_root():
    global expression
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, END)
        entry.insert(END, result)
        expression = str(result)
    except:
        messagebox.showerror("Error", "Invalid Input")

def off():
    root.destroy()

#  BUTTON FRAME a
frame = Frame(root)
frame.pack(expand=True, fill=BOTH)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '%', '+'],
    ['^', '√', 'DEL', '='],
    ['C', 'OFF']
]

for r in range(len(buttons)):
    frame.grid_rowconfigure(r, weight=1)

for c in range(4):
    frame.grid_columnconfigure(c, weight=1)

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "=":
            cmd = equal
        elif text == "C":
            cmd = clear
        elif text == "DEL":
            cmd = delete
        elif text == "√":
            cmd = square_root
        elif text == "OFF":
            cmd = off
        else:
            cmd = lambda t=text: press(t)

        if text == "OFF":
            Button(frame,
                   text=text,
                   font=("Arial", 18),
                   bg="red",
                   fg="white",
                   command=cmd).grid(row=r,
                                     column=0,
                                     columnspan=4,
                                     sticky="nsew",
                                     padx=2,
                                     pady=2)
        elif text == "C":
            Button(frame,
                   text=text,
                   font=("Arial", 18),
                   bg="orange",
                   command=cmd).grid(row=r,
                                     column=0,
                                     sticky="nsew",
                                     padx=2,
                                     pady=2)
        else:
            Button(frame,
                   text=text,
                   font=("Arial", 18),
                   command=cmd).grid(row=r,
                                     column=c,
                                     sticky="nsew",
                                     padx=2,
                                     pady=2)

root.mainloop()