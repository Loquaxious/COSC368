from tkinter import *
from tkinter.ttk import * 

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

window = Tk()
data = StringVar()
data.set("")

keyboard = Frame(window)
keyboard.pack(side='bottom')

r = 0
c = 0
for string in board:
    for ch in list(string):
        b = Button(keyboard, text=ch, command=lambda x=ch: add_char(data, x))
        b.grid(row=r, column=c)
        c+=1
    c=0
    r+=1

text = Label(window, width=100, textvariable=data)
text.pack(side=LEFT, fill=X)

clear = Button(window, text='Clear')
clear.bind('<Button-1>', lambda event : clear_data(data))
clear.pack(side=LEFT)


def clear_data(widget):
    widget.set("")
    
def add_char(widget, char):
    widget.set(widget.get() + char)
    

window.mainloop()