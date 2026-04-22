from missao import Missao
from status import Status

class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, tipo_inimigo: str, inimigos_a_derrotar: int, status=Status.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)
        self.tipo_inimigo = tipo_inimigo
        self.inimigos_a_derrotar = inimigos_a_derrotar

    @property
    def tipo_inimigo(self) -> str:
        return self.__tipo_inimigo

    @tipo_inimigo.setter
    def tipo_inimigo(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O tipo de inimigo deve ser uma string")
        valor_limpo = valor.strip()
        if not valor_limpo:
            raise ValueError("O tipo de inimigo é obrigatório")
        self.__tipo_inimigo = valor_limpo

    @property
    def inimigos_a_derrotar(self) -> int:
        return self.__inimigos_a_derrotar

    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("O número de inimigos deve ser um inteiro")
        if valor <= 0:
            raise ValueError("O número de inimigos deve ser maior que zero")
        self.__inimigos_a_derrotar = valor

    def concluir_missao(self, valor: int) -> bool:
        if valor >= self.inimigos_a_derrotar:
            return super().concluir_missao(valor)
        self.status = Status.FRACASSADA
        print(f'Missão "{self.nome}" fracassada. Inimigos derrotados: {valor}/{self.inimigos_a_derrotar}.')
        return False
