class Item():
    def __init__(self, preco, nome, descricao=None):
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    def __str__(self):
        return f'{self._nome}: R$ {self._preco}'
    
    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco