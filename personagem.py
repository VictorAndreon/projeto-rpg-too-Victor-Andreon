from item import Item, TipoItem

class Personagem:

    def __init__(self, nome: str):
        self.__nome                = nome
        self.__nivel               = 1
        self.__vida_base           = 80
        self.__vida_maxima         = 100
        self.__ataque_base         = 10
        self.__xp                  = 0
        self.__missoes             = []
        self.__missao_ativa        = None
        self.__arma_equipada       = None
        self.__vestimenta_equipada = None
        self.__utilitario_equipado = None
        self.__inventario          = [
            Item("Espada de Ferro",   "Uma espada robusta",         15, TipoItem.ARMA),
            Item("Armadura de Couro", "Proteção leve e resistente", 20, TipoItem.VESTIMENTA),
            Item("Poção de Cura",     "Restaura energia vital",     10, TipoItem.UTILITARIO),
        ]

    @property
    def nome(self):
        return self.__nome

    @property
    def nivel(self):
        return self.__nivel

    @property
    def vida(self):
        bonus = 0
        if self.__vestimenta_equipada:
            bonus += self.__vestimenta_equipada.atributo
        if self.__utilitario_equipado:
            bonus += self.__utilitario_equipado.atributo
        vida_total = int(self.__vida_base * (1 + bonus / 100))
        return min(vida_total, self.__vida_maxima)

    @property
    def xp(self):
        return self.__xp

    @property
    def ataque(self):
        bonus = self.__arma_equipada.atributo if self.__arma_equipada else 0
        return self.__ataque_base + bonus

    @property
    def vida_maxima(self):
        return self.__vida_maxima

    @property
    def ataque_base(self):
        return self.__ataque_base

    @property
    def vida_base(self):
        return self.__vida_base

    @property
    def inventario(self):
        return self.__inventario

    @property
    def arma_equipada(self):
        return self.__arma_equipada

    @property
    def vestimenta_equipada(self):
        return self.__vestimenta_equipada

    @property
    def utilitario_equipado(self):
        return self.__utilitario_equipado

    @nome.setter
    def nome(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser uma string!")
        self.__nome = valor

    def add_item(self, item: Item):
        if not isinstance(item, Item):
            raise TypeError("Apenas objetos do tipo Item podem ser adicionados ao inventário")
        if item not in self.__inventario:
            self.__inventario.append(item)

    def remover_item(self, item: Item):
        if item not in self.__inventario:
            raise ValueError(f"O item '{item.nome}' não está no inventário")
        self.__inventario.remove(item)

    def mostrar_inventario(self):
        print("=== Inventário ===")
        if not self.__inventario:
            print("  (vazio)")
            return
        for item in self.__inventario:
            print(f"  {item}")

    def equiparItens(self, arma: Item, vestimenta: Item, utilitario: Item):
        if not isinstance(arma, Item) or arma.tipo != TipoItem.ARMA:
            raise TypeError("O item de arma deve ser do tipo ARMA")
        if not isinstance(vestimenta, Item) or vestimenta.tipo != TipoItem.VESTIMENTA:
            raise TypeError("O item de vestimenta deve ser do tipo VESTIMENTA")
        if not isinstance(utilitario, Item) or utilitario.tipo != TipoItem.UTILITARIO:
            raise TypeError("O item utilitário deve ser do tipo UTILITARIO")

        if arma not in self.__inventario:
            raise ValueError(f"O item '{arma.nome}' não está no inventário do personagem")
        if vestimenta not in self.__inventario:
            raise ValueError(f"O item '{vestimenta.nome}' não está no inventário do personagem")
        if utilitario not in self.__inventario:
            raise ValueError(f"O item '{utilitario.nome}' não está no inventário do personagem")

        self.__arma_equipada       = arma
        self.__vestimenta_equipada = vestimenta
        self.__utilitario_equipado = utilitario

        return self.ataque, self.vida

    def add_missao(self, missao):
        if missao not in self.__missoes:
            self.__missoes.append(missao)

    def iniciar_missao(self, missao, arma: Item, vestimenta: Item, utilitario: Item):
        if self.__missao_ativa is not None:
            raise ValueError(f"O personagem já está em uma missão: {self.__missao_ativa.nome}")

        if missao not in self.__missoes:
            raise ValueError(f"A missão '{missao.nome}' não está registrada para este personagem")

        self.equiparItens(arma, vestimenta, utilitario)
        self.__missao_ativa = missao
        missao.iniciar_missao()

    def concluir_missao(self, missao, valor):
        if self.__missao_ativa == missao:
            self.__arma_equipada       = None
            self.__vestimenta_equipada = None
            self.__utilitario_equipado = None
            self.__missao_ativa        = None

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
