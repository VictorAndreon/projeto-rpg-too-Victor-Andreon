class Personagem:

    def __init__(self, nome: str):
        self.__nome  = nome
        self.__nivel = 1
        self.__vida  = 100
        self.__xp    = 0

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
    
    @nome.setter
    def nome (self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser uma string!")
        self.nome = valor

    def __str__(self):
            return f"--- Dados do Personagem ---\nNome: {self.nome}\nNível: {self.nivel}\nVida: {self.vida}\nXP: {self.xp}"

    def __eq__(self, outro):
        if not isinstance(outro, Personagem):
            return False
        return self.nome.lower() == outro.nome.lower()
    

if __name__ == "__main__":
    personagem = Personagem("Andreon")
    print(personagem)