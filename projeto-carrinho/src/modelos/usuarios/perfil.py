from datetime import date

class Perfil:
    def __init__(self, nome):
        self._nome = nome
        self._foto = None
        self._data_nascimento = date.today()
        self._descricao = ""
        self._telefone = ""
    
    #Getters e Setters
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome
    
    def get_foto(self):
        return self._foto
    
    def set_foto(self, foto):
        self._foto = foto

    def get_data_nascimento(self):
        return self._data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento
    
    def get_descricao(self):
        return self._descricao
    
    def set_descricao(self, descricao):
        self._descricao = descricao
    
    def get_telefone(self):
        return self._telefone
    
    def set_telefone(self, telefone):
        self._telefone = telefone
