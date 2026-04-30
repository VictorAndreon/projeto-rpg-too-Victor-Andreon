from item import Item, TipoItem

class Personagem:

    def __init__(self, nome: str):
        self.__nome        = nome
        self.__nivel       = 1
        self.__vida_maxima = 100
        self.__vida        = self.__vida_maxima
        self.__ataque      = 10
        self.__xp          = 0
        self.__missoes     = []
        self.__missao_ativa  = None
        self.__itens_ativos  = None
        self.__inventario  = [
            Item("Espada de Ferro",   "Uma espada robusta",        15, TipoItem.ARMA),
            Item("Armadura de Couro", "Proteção leve e resistente", 20, TipoItem.VESTIMENTA),
            Item("Poção de Cura",     "Restaura energia vital",    10, TipoItem.UTILITARIO),
        ]

    @property
    def nome (self):
        return self.__nome
    
    @property
    def nivel (self):
        return self.__nivel
    
    @property
    def vida (self):
        return self.__vida
    
    @property
    def xp (self):
        return self.__xp

    @property
    def ataque(self):
        return self.__ataque

    @property
    def vida_maxima(self):
        return self.__vida_maxima

    @property
    def inventario(self):
        return self.__inventario

    @nome.setter
    def nome (self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser uma string!")
        self.__nome = valor

    def add_missao(self, missao):
        if missao not in self.__missoes:
            self.__missoes.append(missao)

    def iniciar_missao(self, missao, arma: Item, vestimenta: Item, utilitario: Item):
        if self.__missao_ativa is not None:
            raise ValueError(f"O personagem já está em uma missão: {self.__missao_ativa.nome}")

        if missao not in self.__missoes:
            raise ValueError(f"A missão '{missao.nome}' não está registrada para este personagem")

        if not isinstance(arma, Item):
            raise TypeError("arma deve ser uma instância de Item")
        if not isinstance(vestimenta, Item):
            raise TypeError("vestimenta deve ser uma instância de Item")
        if not isinstance(utilitario, Item):
            raise TypeError("utilitario deve ser uma instância de Item")

        if arma.tipo != TipoItem.ARMA:
            raise TypeError("O item de arma deve ser do tipo ARMA")
        if vestimenta.tipo != TipoItem.VESTIMENTA:
            raise TypeError("O item de vestimenta deve ser do tipo VESTIMENTA")
        if utilitario.tipo != TipoItem.UTILITARIO:
            raise TypeError("O item utilitário deve ser do tipo UTILITARIO")

        if arma not in self.__inventario:
            raise ValueError(f"O item '{arma.nome}' não está no inventário do personagem")
        if vestimenta not in self.__inventario:
            raise ValueError(f"O item '{vestimenta.nome}' não está no inventário do personagem")
        if utilitario not in self.__inventario:
            raise ValueError(f"O item '{utilitario.nome}' não está no inventário do personagem")

        self.__ataque += arma.atributo
        self.__vida   += vestimenta.atributo + utilitario.atributo

        self.__missao_ativa = missao
        self.__itens_ativos = (arma, vestimenta, utilitario)

        missao.iniciar_missao()

    def concluir_missao(self, missao, valor):
        if self.__itens_ativos is not None and self.__missao_ativa == missao:
            arma, vestimenta, utilitario = self.__itens_ativos
            self.__ataque -= arma.atributo
            self.__vida   -= vestimenta.atributo + utilitario.atributo
            self.__missao_ativa = None
            self.__itens_ativos = None

        if missao.concluir_missao(valor):
            self.__xp += missao.recompensa

    def exibir_dados(self):
        print(self)

    def __str__(self):
        return (
            f"--- Dados do Personagem ---\n"
            f"Nome: {self.nome}\n"
            f"Nível: {self.nivel}\n"
            f"Vida: {self.vida}/{self.vida_maxima}\n"
            f"Ataque: {self.ataque}\n"
            f"XP: {self.xp}"
        )

    def __eq__(self, outro):
        if not isinstance(outro, Personagem):
            return False
        return self.nome.lower() == outro.nome.lower()
    

if __name__ == "__main__":
    personagem = Personagem("Andreon")
    print(personagem)