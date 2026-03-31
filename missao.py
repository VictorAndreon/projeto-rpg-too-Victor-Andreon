from status import Status

class Missao:
    def __init__(self, nome: str, descricao: str, recompensa: int, status: str = Status.PENDENTE):
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
    def status(self, valor: Status):
        if not isinstance(valor, Status):
            raise TypeError("O status deve ser um Status")

        status_atual = self.__status

        if status_atual is not None:
            if status_atual == Status.PENDENTE and valor != Status.EM_ANDAMENTO:
                raise ValueError("Missão PENDENTE só pode ir para EM ANDAMENTO")
            if status_atual == Status.EM_ANDAMENTO and valor not in (Status.CONCLUIDA, Status.FRACASSADA):
                raise ValueError("Missão EM ANDAMENTO só pode ir para CONCLUIDA ou FRACASSADA")

        self.__status = valor

    def __str__(self):
            return f"--- Dados da Missão ---\nNome: {self.nome}\nDescrição: {self.descricao}\nRecompensa: {self.recompensa}\nStatus: {self.status.name}"

    def __eq__(self, outro):
        if not isinstance(outro, Missao):
            return False
        return self.nome.lower() == outro.nome.lower()
    
    def iniciar_missao(self):
        if self.__status != Status.PENDENTE:
            raise ValueError("Essa missão não pode ser iniciada novamente!")
        self.status = Status.EM_ANDAMENTO
        print(f'A missão {self.nome} começou! Objetivo central da missão: {self.descricao}.')

    def concluir_missao(self):
        if self.__status != Status.EM_ANDAMENTO:
            raise ValueError("Essa missão não pode ser concluída.")
        self.__status = Status.CONCLUIDA
        print(f'Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira.')

    def exibir_dados(self):
        print(self)