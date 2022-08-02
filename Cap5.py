

class Color:
    def __init__(self, valor_rgb, nome):
        self._valor_rgb = valor_rgb
        self._nome = nome
    
    def define_nome(self, nome):
        self._nome = nome
    
    def obter_nome(self):
        return self._nome
        