from page_model import *

class Home(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout()
    
    def layout(self):
        upper_bar = ttk.Frame(self, height=158, style="Primary.TFrame")
        upper_bar.pack(fill=X)
        search_bar = ttk.Entry(upper_bar, width=150)
        search_bar.pack(pady=43, padx=200)
        collapse_bar = ttk.Frame(upper_bar, height=70, style="Secondary.TFrame")
        collapse_bar.pack(fill=X)
        usable_area = ttk.Frame(self, width=1768, height=750, style="Secondary.TFrame")
        usable_area.pack(side=BOTTOM, pady=76, padx=76)

if __name__ == "__main__":
    window = Window(title="Home Page")
    Home(window)
    window.mainloop()
