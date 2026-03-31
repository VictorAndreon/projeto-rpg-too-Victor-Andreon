from missao import Missao
from status import Status

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa, item_necessario, quantidade_item, status=Status.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)
        self.item_necessario = item_necessario
        self.quantidade_item = quantidade_item

    @property
    def item_necessario(self) -> str:
        return self.__item_necessario

    @item_necessario.setter
    def item_necessario(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O item necessário deve ser uma string")
        valor_limpo = valor.strip()
        if not valor_limpo:
            raise ValueError("O item necessário é obrigatório")
        self.__item_necessario = valor_limpo

    @property
    def quantidade_item(self) -> int:
        return self.__quantidade_item

    @quantidade_item.setter
    def quantidade_item(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("A quantidade do item deve ser um inteiro")
        if valor <= 0:
            raise ValueError("A quantidade do item deve ser maior que zero")
        self.__quantidade_item = valor
