import sys
import os
from tkinter import *
import main

window=Tk()
window.title("Running Python Script")
window.geometry('550x200')

def run():
    os.system('python C:/Users/user/handstracking-master/flappyBird.py')

def run2():
    os.system('python C:/Users/user/NEAT-Flappy-Bird-master/flappy_bird.py')

btn = Button(window, text="Hand Bird", bg="blue", fg="white",command=run)
btn.grid(column=0, row=0)

btn = Button(window, text="GA Bird", bg="blue", fg="white",command=run2)
btn.grid(column=1, row=0)

window.mainloop()