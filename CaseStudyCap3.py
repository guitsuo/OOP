

class Propriedade:
    # Estamos adicionando "Kwargs" porque sabemos que será utilizado em uma situaçã ode múltipla herança 
    def __init__(self, metros_quadrados, camas, banheiros, **kwargs):
        super().__init__(**kwargs)
        self.metros_quadrados = metros_quadrados
        self.n_camas = camas
        self.n_banheiros = banheiros 

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
                    banheiros = input("Adicione o numero de banheiros")
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

        print(f"n_historias: {self.n_historias}")
        print(f"garagem: {self.garagem}")
        print(f"cerca: {self.cerca}")

    @staticmethod
    def prompt_init():
        parent_init = Propriedade.prompt_init()
        cerca = obter_input_valido("O jardim tem cerca?", Casa.cercas_validas)
        garagem = obter_input_valido("Há uma garagem?", Casa.garagens_validas)

        n_historias = input("Quantas historias? ")

        parent_init.update({
            "cerca": cerca,
            "garagem": garagem,
            "n_historias": n_historias
        })
        return parent_init


class Compra:
    # Por que estamos colocando super().__init__ ?
    # R: Porque vão ser combinadas com outras classes e não sabemos em que ordem as chamadas "super" vão ser feitas
    def __init__(self, preco = '', taxas = '', **kwargs):
        super().__init__(**kwargs)
        self.preco = preco
        self.taxas = taxas

    def display(self):
        super().display()
        print("----- Detalhes da compra  ------")
        print(f"Preço de venda: {self.preco}")
        print(f"Taxas estimadas: {self.taxas}")

    @staticmethod
    def prompt_init():
        return dict(
            preco = input("Qual o preço de venda?"),
            taxas = input("Qual as taxas estimadas?")
        )

class Aluguel:
    def __init__(self, mobiliada = '', utilidades = '', aluguel = '', **kwargs):
        super().__init__(**kwargs)
        self.mobiliada = mobiliada
        self.aluguel = aluguel
        self.utilidades = utilidades

    def display(self):
        super().display()
        print("Detalhes de aluguel")
        print(f"Aluguel: {self.aluguel}")
        print(f"Utilidades estimadas: {self.utilidades}")
        print(f"mobiliada: {self.mobiliada}")

    @staticmethod
    def prompt_init():
        return dict(
            aluguel = input("Qual o aluguel mensal?"),
            utilidades = input(
                "Quais são as utildiades estimadas"
            ),
            mobiliada = obter_input_valido(
                "A propriedade é mobiliada?", ("sim", "nao")
            )
        )

class CasaAluguel(Aluguel, Casa):
    @staticmethod 
    def prompt_init():
        init = Casa.prompt_init()
        init.update(Aluguel.prompt_init())
        return init 

class ApartamentoAluguel(Aluguel, Apartamento):
    @staticmethod
    def prompt_init():
        init = Apartamento.prompt_init()
        init.update(Aluguel.prompt_init())
        return init 

class ApartamentoCompra(Compra, Apartamento):
    @staticmethod
    def prompt_init():
        init = Apartamento.prompt_init()
        init.update(Compra.prompt_init())
        return init

class CasaCompra(Compra, Casa):
    @staticmethod
    def prompt_init():
        init = Compra.prompt_init()
        init.update(Compra.prompt_init())
        return init

class Agente:
    def __init__(self):
        self.lista_propriedade = []

    
    def display_propriedades(self):
        for propriedade in self.lista_propriedade:
            propriedade.display()

    tipo_mapa = {
        ("casa", "aluguel"): CasaAluguel,
        ("casa", "compra"): CasaCompra,
        ("apartamento", "aluguel"): ApartamentoAluguel,
        ("apartamento", "compra"): ApartamentoCompra
    }

    def adiciona_propriedade(self):
        tipo_propriedade = obter_input_valido(
            "Que tipo de propriedade",
            ("casa", "apartamento")).lower()
        tipo_pagamento = obter_input_valido(
            "Que tipo de pagamento?",
            ("compra", "aluguel")).lower()
        
        ClassePropriedade = self.tipo_mapa[(tipo_propriedade, tipo_pagamento)]
        init_args = ClassePropriedade.prompt_init()
        self.lista_propriedade.append(ClassePropriedade(**init_args))

        

init = CasaAluguel.prompt_init()

casa = CasaAluguel(**init)
casa.display()