from enum import Enum


class TipoItem(Enum):
    ARMA       = "ARMA"
    VESTIMENTA = "VESTIMENTA"
    UTILITARIO = "UTILITARIO"


class Item:

    def __init__(self, nome: str, descricao: str, atributo: int, tipo: TipoItem):
        self.nome     = nome
        self.descricao = descricao
        self.atributo  = atributo
        self.tipo      = tipo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser uma string")
        valor_limpo = valor.strip()
        if not valor_limpo:
            raise ValueError("O nome é obrigatório")
        self.__nome = valor_limpo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("A descrição deve ser uma string")
        self.__descricao = valor

    @property
    def atributo(self):
        return self.__atributo

    @atributo.setter
    def atributo(self, valor: int):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("O atributo deve ser um inteiro")
        if valor <= 0:
            raise ValueError("O atributo deve ser maior que zero")
        self.__atributo = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor: TipoItem):
        if not isinstance(valor, TipoItem):
            raise TypeError("O tipo deve ser um TipoItem")
        self.__tipo = valor

    def __str__(self):
        return f"[{self.tipo.value}] {self.nome} — {self.descricao} (+{self.atributo})"

    def __eq__(self, outro):
        if not isinstance(outro, Item):
            return False
        return self.nome.lower() == outro.nome.lower()
