

class Propriedade:

    def __init__(self, metros_quadrados, n_camas, n_banheiros, **kwargs):
        self.metros_quadrados = metros_quadrados
        self.n_camas = n_camas
        self.n_banheiros = n_banheiros 

    def display(self):
        '''
        Deve representar as características da propriedade
        '''
        return f'Esta propriedade possui {self.metros_quadrados}, {self.n_camas} e {self.n_banheiros}'

    @staticmethod
    def prompt_init():
        return dict(metros_quadrados = input("Adicione os metros quadrados: "),
                    camas = input("Adicione o numero de camas"),
                    banhos = input("Adicione o numero de banheiros")
        )
    #prompt_init = staticmethod(prompt_init)


class Apartamento(Propriedade):
    def __init__(self, metros_quadrados, n_camas, n_banheiros, sacada, lavanderia):
        super().__init__(metros_quadrados, n_camas, n_banheiros)
        self.sacada = sacada
        self.lavanderia = lavanderia 

class Casa(Propriedade):
    def __init__(self, metros_quadrados, n_camas, n_banheiros, n_historias, garagem, cerca):
        super().__init__(metros_quadrados, n_camas, n_banheiros)
        self.n_historias = n_historias
        self.garagem = garagem
        self.cerca = cerca 


