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
        self.nome = valor

    def add_missao(self, missao):
        if missao not in self.__missoes:
            self.__missoes.append(missao)

    def concluir_missao(self, missao, valor):
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