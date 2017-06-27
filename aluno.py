

class aluno:
    def __init__(self,nome,CPF):
        self.nome = nome
        self.CPF = CPF

    def getNome(self):
        return self.nome
    def setNome(self,novoNome):
        self.nome = novoNome

    def getCPF(self):
        return self.CPF