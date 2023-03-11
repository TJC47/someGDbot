from tkinter import *
from tkinter import ttk
import time
from threading import Thread
running = True
comment = "hi"
lastsaid = "hi"
def start():
    global running
    gui = Tk()
    gui.title("GD Comment Bot")
    ttk.Label(gui, text="Last User message:").pack()
    te = ttk.Label(gui, text=comment)
    te.pack()
    ttk.Label(gui, text="Last Bot message:").pack()
    te2 = ttk.Label(gui, text=lastsaid)
    te2.pack()
    while running:
        try:
            te.config(text=comment)
            te2.config(text=lastsaid)
            gui.update()
            time.sleep(0.1)
        except:
            running = False
print("[GUI] LOADED")
