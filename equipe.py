#coding: utf-8
from aluno import aluno
class equipe:
    def __init__(self,projeto):
        self.projeto = projeto
        self.listaAluno = []

    def cadastrar(self,nome,CPF):
        a = aluno(nome,CPF)
        self.listaAluno.append(a)
    def  remover(self,CPF):
        estudante = self.procura(CPF)
        if estudante == None:
            return
        else:
            self.listaAluno.remove(estudante)
    def procura(self,CPF):
        for i in range(len(self.listaAluno)):
            if self.listaAluno[i].getCPF() == CPF:
                return self.listaAluno[i]
        return None
    def mostrar(self):
        for i in range(len(self.listaAluno)):
            print "Nome da equipe: DLEI"
            print "Aluno: %s CPF: %i" % (self.listaAluno[i].getNome(),self.listaAluno[i].getCPF())