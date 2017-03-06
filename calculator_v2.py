# Import modules
from tkinter import *
from tkinter import ttk

# Create the window and give it a title
root = Tk()
root.title("Calculator")

# Create the class for the number buttons
class NumberButton(Button):
    def __init__(self, text):
        super().__init__(number_frame, text=text, command=self.append)
        self.text = text
    
    def append(self):
        entry_text.set(entry_text.get() + self.text)

# Create the three frames
# Frame for the entry box
entry_frame = Frame(root)
entry_frame.grid(row=0, column=0, columnspan=2)

# Frame for the number buttons
number_frame = Frame(root)
number_frame.grid(row=1, column=0, sticky="NSEW")

# Frame for the operator buttons
operator_frame = Frame(root)
operator_frame.grid(row=1, column=1)

# Create the text entry box and assign it a textvariable
entry_text = StringVar()
entry_field = Entry(entry_frame, textvariable=entry_text)
entry_field.grid(row=0, column=0)

# Create the ten number buttons
button_1 = NumberButton(text="1")
button_1.grid(row=0, column=0, sticky="NSEW")

button_2 = NumberButton(text="2")
button_2.grid(row=0, column=1, sticky="NSEW")

button_3 = NumberButton(text="3")
button_3.grid(row=0, column=2, sticky="NSEW")

button_4 = NumberButton(text="4")
button_4.grid(row=1, column=0, sticky="NSEW")

button_5 = NumberButton(text="5")
button_5.grid(row=1, column=1, sticky="NSEW")

button_6 = NumberButton(text="6")
button_6.grid(row=1, column=2, sticky="NSEW")

button_7 = NumberButton(text="7")
button_7.grid(row=2, column=0, sticky="NSEW")

button_8 = NumberButton(text="8")
button_8.grid(row=2, column=1, sticky="NSEW")

button_9 = NumberButton(text="9")
button_9.grid(row=2, column=2, sticky="NSEW")

button_0 = NumberButton(text="0")
button_0.grid(row=3, column=1, sticky="NSEW")

root.mainloop()
