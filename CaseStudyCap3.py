

class Propriedade:
    # Estamos adicionando "Kwargs" porque sabemos que será utilizado em uma situaçã ode múltipla herança 
    def __init__(self, metros_quadrados, n_camas, n_banheiros, **kwargs):
        super().__init__(**kwargs)
        self.metros_quadrados = metros_quadrados
        self.n_camas = n_camas
        self.n_banheiros = n_banheiros 

    def display(self):
        '''
        Deve representar as características da propriedade
        '''
        return f'Esta propriedade possui {self.metros_quadrados}, {self.n_camas} e {self.n_banheiros}'

    # Métodos estáticos são associados apenas com uma classe ao invés de uma instância de objeto em específico
    # Por isso, não possuem argumento self
    @staticmethod
    def prompt_init():
        return dict(metros_quadrados = input("Adicione os metros quadrados: "),
                    camas = input("Adicione o numero de camas"),
                    banhos = input("Adicione o numero de banheiros")
        )
    #prompt_init = staticmethod(prompt_init)


class Apartamento(Propriedade):

    lavanderias_validas = ("privativa", "publica" , "none")
    sacadas_validas = ("sim", "não", "solarium")

    def __init__(self, sacada, lavanderia, **kwargs):
        super().__init__(**kwargs)
        self.sacada = sacada
        self.lavanderia = lavanderia 

    def display(self):
        super().display()
        print("----- Detalhes do apartamento ------")
        print(f"lavanderia: {self.lavanderia}")
        print(f"sacadas: {self.sacada}")

    def prompt_init():
        parent_init = Propriedade.prompt_init()
        lavanderia = obter_input_valido('''
        Que facilidas de lavanderia a propriedade tem?
        ''',
        Apartamento.lavanderias_validas
        )

        sacada = obter_input_valido('''
        O Apartamento possui sacada?
        ''', 
        Apartamento.sacadas_validas
        )
        return parent_init
    prompt_init = staticmethod(prompt_init)


def obter_input_valido(string_entrada, opcoes_validas):
    string_entrada += " ({})".format(", ").join(opcoes_validas)
    resposta = input(string_entrada)

    while resposta.lower() not in opcoes_validas:
        resposta = input(string_entrada)
    return resposta

class Casa(Propriedade):
    garagens_validas = ("anexada", "desanexada","nulo")
    cercas_validas = ("sim","nao")

    def __init__(self,  n_historias, garagem, cerca, **kwargs):
        super().__init__(**kwargs)
        self.n_historias = n_historias
        self.garagem = garagem
        self.cerca = cerca 

    def display(self):
        super().display()
        print("----- Detalhes da casa  ------")
        print(f"n_historias: {self.lavanderia}")
        print(f"sacadas: {self.sacada}")

    def prompt_init():
        parent_init = Propriedade.prompt_init()
        cerca = obter_input_valido("O jardim tem cerca?", Casa.cercas_validas)
        garagem = obter_input_valido("Há uma garagem?", Casa.garagens_validas)

t = Apartamento("sim", "privativa").display()
print(t)

