from tkinter import *
from tkinter.ttk import * 

def clicked():
    print('clicked')


master = Tk()
c = Canvas(master, width=200, height=200)
c.pack()
c.create_line(0, 0, 200, 100, tag='cool')
c.create_line(0, 100, 200, 0, fill="red", dash=(4, 4), tag='cool')
rect = c.create_rectangle(50, 25, 150, 75, fill="blue", tag='hot')
c.itemconfigure('cool', fill='blue')
c.itemconfigure(rect, fill='red')
c.addtag_withtag('red', ALL)
c.itemconfigure('red', fill='green')
c.tag_bind(rect, "<ButtonPress-1>", clicked)
c.tag_bind('cool', "<ButtonPress-1>", print('bar'))

master.mainloop()