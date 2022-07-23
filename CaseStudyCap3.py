

class Propriedade:

    def __init__(self, metros_quadrados, n_camas, n_banheiros):
        self.metros_quadrados = metros_quadrados
        self.n_camas = n_camas
        self.n_banheiros = n_banheiros 

class Apartamento(Propriedade):
    def __init__(self, metros_quadrados, n_camas, n_banheiros):
        super().__init__(metros_quadrados, n_camas, n_banheiros)
        self.sacada = self.sacada
        self.lavanderia = self.lavanderia 




class Agent:
    pass