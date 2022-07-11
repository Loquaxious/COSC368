from tkinter import *
from tkinter.ttk import *  
window = Tk()
frame = Frame(window, height=32, width=32)
frame.pack_propagate(0) # don't shrink
frame.grid(row=0, column=0)
button = Button(frame, text="Hi")
button.pack(fill=BOTH, expand=1)
lbl = Label(frame)
lbl.pack(side=TOP)
lbl.config(text="Hello")
window.mainloop()