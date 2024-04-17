from Disciplina import Disciplina

class Curso:
    cursos_disponiveis = []

    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []
        Curso.cursos_disponiveis.append(self)

    def adicionarDisciplina(self, nome_disciplina, sala_numero):
        nova_disciplina = Disciplina(nome_disciplina, sala_numero)
        self.disciplinas.append(nova_disciplina)
        print(f"Disciplina '{nome_disciplina}' adicionada ao curso '{self.nome}'.")

    def definirSala(self, nome_disciplina, nova_sala_numero):
        for disciplina in self.disciplinas:
            if disciplina.nome == nome_disciplina:
                disciplina.sala = nova_sala_numero
                print(f"Sala da disciplina '{nome_disciplina}' alterada para '{nova_sala_numero}'.")
                return
        print(f"Disciplina '{nome_disciplina}' não encontrada no curso '{self.nome}'.")

    def listarDisciplinas(self):
        print(f"Disciplinas do curso '{self.nome}':")
        for disciplina in self.disciplinas:
            print(f"Disciplina: {disciplina.nome}, Sala: {disciplina.sala}")
