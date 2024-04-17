from Curso import Curso

class Aluno:
    def __init__(self):
        self.nome = input("Digite o nome do aluno: ")
        self.curso = None

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

