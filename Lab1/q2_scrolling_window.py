from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

window = Tk()

text = Text(window, height=10, width=24, wrap='none')
text.grid(row=0, column=0)
#text.pack(side='left')

vsb = Scrollbar(window, command=text.yview)
vsb.grid(row=0, column=1, rowspan=1, sticky="ns")
#vsb.pack(side='right', fill='y')

hsb= Scrollbar(window, orient='horizontal', command=text.xview)
hsb.grid(row=1, column=0, columnspan=1, sticky="ew")
#hsb.pack(side='bottom', fill='x')

window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)

text.focus()
window.mainloop()