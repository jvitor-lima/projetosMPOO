from Curso import Curso
from Endereco import Endereco
class Professor:
    idProfessor = 0

    def __init__(self):
        self.nome = input("Digite o nome do professor: ")
        Professor.idProfessor += 1
        self.idProfessor = f"P{Professor.idProfessor:04d}"
        self.curso = None
        self.endereco = Endereco()
        self.endereco.cadastrarEndereco(
            input("Digite a rua: "),
            input("Digite o número: "),
            input("Digite o bairro: "),
            input("Digite o CEP: "),
            input("Digite o complemento (opcional): "),
            input("Digite o município: "),
            input("Digite o estado: ")
        )
        print(f"Nome: {self.nome}\nEndereço: {self.endereco.rua}, {self.endereco.numero}, {self.endereco.bairro}, CEP: {self.endereco.cep}")
        print("Professor cadastrado com sucesso!")


    def adicionarDisciplina(self, nome_disciplina, sala_numero):
        if self.curso is None:
            print("Você precisa criar um curso primeiro.")
            return
        self.curso.adicionarDisciplina(nome_disciplina, sala_numero)

    def cadastrarProfessor(self):
        if self.curso is None:
            return
        print(f"Nome: {self.nome}\nID Professor: {self.idProfessor}\nCurso: {self.curso.nome}")
        print("Professor cadastrado com sucesso!")