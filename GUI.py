# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Button, StringVar, Listbox

class GUI:

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.listBox1 = Listbox(master, selectmode = "SINGLE")
        self.listBox1.pack()
        
        
#top = tkinter.Tk()
## Code to add widgets will go here...
#tkinter.Label(top, text="This is our first GUI!").pack()
#lB = tkinter.Listbox(top)
#for count, i in enumerate(reseau.listBusStop):
#    lB.insert(count, i.name)
#lB.pack()
#top.mainloop()