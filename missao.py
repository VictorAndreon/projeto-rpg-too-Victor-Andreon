class Missao:
    STATUS_LISTA = ["PENDENTE", "EM ANDAMENTO", "CONCLUIDA"]

    def __init__(self, nome: str, descricao: str, recompensa: int, status: str = "PENDENTE"):
        self._Missao__status = None  # Inicialização explícita do campo privado
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.status = status

    @property 
    def nome(self):
        return self.__nome.title()
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def recompensa(self):
        return self.__recompensa
    
    @property
    def status(self):
        return self.__status
    
    @nome.setter
    def nome(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser uma string")
        valor_limpo = valor.strip()
        if not valor_limpo:
            raise ValueError("O Nome é obrigatório")
        self.__nome = valor_limpo

    @descricao.setter
    def descricao(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("A descrição deve ser uma string")
        self.__descricao = valor

    @recompensa.setter
    def recompensa(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("A recompensa deve ser um inteiro")
        if not (0 <= valor <= 50):
            raise ValueError("A recompensa deve ser entre 0 e 50")
        self.__recompensa = valor
        
    @status.setter
    def status(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O status deve ser uma string")
        
        if valor not in self.STATUS_LISTA:
            raise ValueError(f"Status inválido. Use: {self.STATUS_LISTA}")

        status_atual = self._Missao__status

        if status_atual is not None:
            if status_atual == 'PENDENTE' and valor != 'EM ANDAMENTO':
                raise ValueError("Missão PENDENTE só pode ir para EM ANDAMENTO")
            if status_atual == 'EM ANDAMENTO' and valor != 'CONCLUIDA':
                raise ValueError("Missão EM ANDAMENTO só pode ir para CONCLUIDA")
        
        self.__status = valor

    def __str__(self):
            return f"--- Dados da Missão ---\nNome: {self.nome}\nDescrição: {self.descricao}\nRecompensa: {self.recompensa}\nStatus: {self.status}"

    def __eq__(self, outro):
        if not isinstance(outro, Missao):
            return False
        return self.nome.lower() == outro.nome.lower()
    

if __name__ == "__main__":
    missao = Missao("derrotar os goblins", "Derrotar os goblins malvados do reino", 50)
    missao.status = 'EM ANDAMENTO'
    print(missao)
