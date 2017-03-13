# Import modules
from tkinter import *
from tkinter import ttk

# Create the window and give it a title
root = Tk()
root.title("Calculator")

# Create the class for the number buttons
class NumberButton(Button):
    def __init__(self, parent, text):
        super().__init__(parent, text=text, command=self.append)
        self.text = text
        self.parent = parent
    
    def append(self):
        if entry_text.get() == "0":
            entry_text.set("")
        entry_text.set(entry_text.get() + self.text)

def evaluate():
    entry_text.set(eval(entry_text.get()))

def clear():
    entry_text.set("0")

# Create the three frames
# Frame for the entry box
entry_frame = Frame(root)
entry_frame.grid(row=0, column=0, columnspan=2)
entry_frame.grid_rowconfigure(0, weight=1)
entry_frame.grid_columnconfigure(0, weight=1)

# Frame for the number buttons
number_frame = Frame(root)
number_frame.grid(row=1, column=0, sticky="NSEW")
for row in range(4):
    number_frame.grid_rowconfigure(row, weight=4)
for column in range(3):
    number_frame.grid_columnconfigure(column, weight=3)

# Frame for the operator buttons
operator_frame = Frame(root)
operator_frame.grid(row=1, column=1)
for row in range(3):
    operator_frame.grid_rowconfigure(row, weight=3)
for column in range(2):
    operator_frame.grid_columnconfigure(column, weight=4)

# Create the text entry box and assign it a textvariable
entry_text = StringVar()
entry_field = Entry(entry_frame, textvariable=entry_text, justify="right")
entry_field.grid(row=0, column=0, sticky="NSEW")

# Create the ten number buttons

button_list = [NumberButton(number_frame, text=str(i)) for i in range(10)]

number_counter = 1

for row in range(3):
    for column in range(3):
        button_list[number_counter].grid(row=row, column=column, sticky="NSEW")
        number_counter += 1

button_list[0].grid(row=3, column=1, sticky="NSEW")

button_point = NumberButton(number_frame, text=".")
button_point.grid(row=3, column=0, sticky="NSEW")

button_clear = Button(operator_frame, text="C", command=clear)
button_clear.grid(row=2, column=0, sticky="NSEW")

button_evaluate = Button(operator_frame, text="=", command=evaluate)
button_evaluate.grid(row=2, column=1, sticky="NSEW")

sign_list = [" + ", " - ", " * ", " / "]
operator_list = []

for sign in sign_list:
    operator_list.append(NumberButton(operator_frame, text=sign))

operator_counter = 0

for row in range(2):
    for column in range(2):
        operator_list[operator_counter].grid(row=row, column=column, sticky="NSEW")
        operator_counter += 1

root.mainloop()
