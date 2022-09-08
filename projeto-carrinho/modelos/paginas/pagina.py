from cgitb import text
from unittest.mock import DEFAULT
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

class MinhaUI():
    def _construir_base(self):
        janela = ttk.Window(
            title="Minha GUI Mauá",
            size= (1440,1024),
            minsize= (600,300),
            maxsize= (1800,900),
            alpha=1.0
        )
        janela.iconphoto(False, PhotoImage(file='logo.png'))
        return janela

    def __init__(self) -> None:
            self.base = self._construir_base()

    def run(self):
        self.base.mainloop()

app = MinhaUI()
app.run()