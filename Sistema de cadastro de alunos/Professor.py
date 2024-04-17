from Curso import Curso

class Professor:
    idProfessor = 0

    def __init__(self):
        self.matricula = ""
        self.curso = None
        self.nome = input("Digite o nome: ")

    def criarCurso(self, nome_curso):
        if self.curso is None:
            self.curso = Curso(nome_curso)
            print(f"Curso '{nome_curso}' criado com sucesso.")
        else:
            print("Você já está vinculado a um curso.")

    def adicionarDisciplina(self, nome_disciplina, sala_numero):
        if self.curso is None:
            print("Você precisa criar um curso primeiro.")
            return
        self.curso.adicionarDisciplina(nome_disciplina, sala_numero)

    def cadastrarProfessor(self):
        if self.curso is None:
            print("Você precisa criar um curso primeiro.")
            return
        Professor.idProfessor += 1
        self.matricula = f"{Professor.idProfessor:04d}"
        print(f"Nome: {self.nome}\nMatrícula: {self.matricula}\nCurso: {self.curso.nome}")
        print("Professor cadastrado com sucesso!")
