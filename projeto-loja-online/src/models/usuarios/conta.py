class Conta:
    def __init__(self, id=None, historico=[]):
        self._id = id
        self._historico = historico
    
    def get_historico(self):
        return self._historico