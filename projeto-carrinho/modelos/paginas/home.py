from pagina import Pagina

class Home(Pagina):
    def _construir_base(self):
        janela = super()._construir_base()
        janela.title("Home")
        return janela
    
app = Home()
app.run()
