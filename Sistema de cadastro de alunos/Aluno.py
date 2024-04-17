from Curso import Curso
from Endereco import Endereco
class Aluno:
    idAluno = 0

    def __init__(self):
        self.nome = input("Digite o nome do aluno: ")
        Aluno.idAluno += 1
        self.matricula = 2024 + Aluno.idAluno
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
        print("Aluno cadastrado com sucesso!")
        
    def verCursosDisponiveis(self):
        print("Cursos Disponíveis:")
        for i, curso in enumerate(Curso.cursos_disponiveis, 1):
            print(f"{i}. {curso.nome}")

    def selecionarCurso(self, numero_curso):
        if 1 <= numero_curso <= len(Curso.cursos_disponiveis):
            self.curso = Curso.cursos_disponiveis[numero_curso - 1]
            print(f"Curso selecionado: {self.curso.nome}")
        else:
            print("Número de curso inválido.")

    def mostrarDisciplinas(self):
        if self.curso:
            print(f"Disciplinas do curso '{self.curso.nome}':")
            for disciplina in self.curso.disciplinas:
                print(f"Disciplina: {disciplina.nome}, Sala: {disciplina.sala}")
        else:
            print("Nenhum curso selecionado.")