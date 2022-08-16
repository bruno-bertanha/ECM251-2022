class Carrinho:
    def __init__(self):
        self._itens = []
    
    def get_valpr_total(self):
        valor_total = 0
        for item in self._itens:
            valor_total += item.get_preco()
        return valor_total
    
    def get_tamanho(self):
        return len(self._itens)
    
    def adicionar_item(self, item):
        self._itens.append(item)
    
    def remover_item(self, item):
        self._itens.remove(item)