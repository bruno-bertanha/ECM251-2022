from cgitb import text
from unittest.mock import DEFAULT
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

class Pagina():
    def _construir_base(self):
        janela = ttk.Window(
            title="",
            size= (1366,768),
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

if __name__ == "__main__":
    app = Pagina()
    app.run()
