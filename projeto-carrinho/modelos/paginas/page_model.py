from cgitb import text
from unittest.mock import DEFAULT
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

class Page(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)

class Window(ttk.Window):
    def __init__(self, title="Página", **kwargs):
        super().__init__(title=title,
                         size=(1920,1080),
                         **kwargs)
        self.iconphoto(False, PhotoImage(file="logo.png"))

if __name__ == "__main__":
    window = Window()
    Page(window)
    window.mainloop()      