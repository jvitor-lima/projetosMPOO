import os
from datetime import date
from Pessoa import Pessoa
from Curso import Curso
import Endereco


class Professor(Pessoa):
    idProfessor = 0

    def __init__(self):
        super().__init__()
        self.matricula = ""
        self.curso = Curso("")

    def cadastrarProfessor(self):
        self.curso.novoCurso(input("Digite o nome do curso: "))
        Professor.idProfessor += 1
        data = date.today()
        data_formatada = data.strftime("%Y%m%d")
        self.matricula = f"{data_formatada}0{Professor.idProfessor}"
        print(f"Nome: {self.nome}\nMatrícula: {self.matricula}\nCurso: {self.curso.nome}\nEndereço: {
              self.endereco.rua}, {self.endereco.numero}, {self.endereco.bairro}, CEP: {self.endereco.cep}")
        print("Professor cadastrado com sucesso!")
