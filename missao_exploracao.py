from missao import Missao
from status import Status

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, regiao_destino, distancia_em_km, status=Status.PENDENTE):
        super().__init__(nome, descricao, recompensa, status)
        self.regiao_destino = regiao_destino
        self.distancia_em_km = distancia_em_km

    @property
    def regiao_destino(self) -> str:
        return self.__regiao_destino

    @regiao_destino.setter
    def regiao_destino(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("A região de destino deve ser uma string")
        valor_limpo = valor.strip()
        if not valor_limpo:
            raise ValueError("A região de destino é obrigatória")
        self.__regiao_destino = valor_limpo

    @property
    def distancia_em_km(self) -> float:
        return self.__distancia_em_km

    @distancia_em_km.setter
    def distancia_em_km(self, valor: float):
        if not isinstance(valor, (int, float)):
            raise TypeError("A distância deve ser um número")
        if valor <= 0:
            raise ValueError("A distância deve ser maior que zero")
        self.__distancia_em_km = float(valor)
