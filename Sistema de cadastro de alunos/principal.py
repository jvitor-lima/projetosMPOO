from Professor import Professor
from Aluno import Aluno
from Curso import Curso

usuario1 = Professor()
curso1 = Curso("Sistemas de Informação")
usuario1.cadastrarProfessor()
curso1.adicionarDisciplina("Lógica de Programação", "Sala 1")
curso1.adicionarDisciplina("MPOO", "Sala 12")
curso1.definirSala("MPOO", "Sala 15")
curso1.listarDisciplinas()

usuario2 = Aluno()
usuario2.verCursosDisponiveis()
usuario2.selecionarCurso(1)
usuario2.mostrarDisciplinas()
