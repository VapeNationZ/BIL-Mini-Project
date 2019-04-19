import sys
import os
from tkinter import *

window=Tk()

window.title("AGnes Program using Java")
window.geometry('550x200')

def run():
    os.system('java agnes')

btn = Button(window, text="Run Agglomerative Clustering", bg="black", fg="black",command=run)
btn.grid(column=0, row=0)

window.mainloop()