import os
from datetime import date
from Pessoa import Pessoa
from Curso import Curso
import Endereco


class Aluno(Pessoa):
    idAluno = 0

    def __init__(self):
        super().__init__()
        self.matricula = ""
        self.curso = Curso("")

    def cadastrarAluno(self):
        self.curso.novoCurso(input("Digite o nome do curso: "))
        Aluno.idAluno += 1
        data = date.today()
        data_formatada = data.strftime("%Y%m%d")
        self.matricula = f"{data_formatada}0{Aluno.idAluno}"
        print(f"Nome: {self.nome}\nMatrícula: {self.matricula}\nCurso: {self.curso.nome}\nEndereço: {
              self.endereco.rua}, {self.endereco.numero}, {self.endereco.bairro}, CEP: {self.endereco.cep}")
        print("Aluno cadastrado com sucesso!")
