# Import modules
from tkinter import *
from tkinter import ttk

# Create the frames
root = Tk()
root.title("Calculator")

entry_frame = Frame(root)
entry_frame.grid(row=0, column=0, columnspan=2)

number_frame = Frame(root)
number_frame.grid(row=1, column=0)

operator_frame = Frame(root)
operator_frame.grid(row=1, column=1)


class NumberButton(Button):
    
  def command(self):
    entry_text += text

entry_text = StringVar()
entry_field = Entry(entry_frame, textvariable=entry_text)
entry_field.grid(row=0, column=0)

button_1 = NumberButton(root, text="1")
button_1.grid(row=0, column=0, sticky="NSEW")

button_2 = NumberButton(root, text="2")
button_2.grid(row=0, column=1, sticky="NSEW")

root.mainloop()
