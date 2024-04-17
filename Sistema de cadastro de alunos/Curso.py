class Curso:
    cursos = []

    def __init__(self, nome):
        self.nome = nome

    def novoCurso(self, nome_curso):
        self.cursos.append(nome_curso)
        print(f"Curso '{nome_curso}' criado com sucesso!")

    def listarCursos(self):
        if self.cursos:
            print("Cursos cadastrados:")
            for curso in self.cursos:
                print(curso)
        else:
            print("Nenhum curso cadastrado.")
