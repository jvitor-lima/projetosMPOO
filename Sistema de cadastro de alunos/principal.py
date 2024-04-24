from Professor import Professor
from Aluno import Aluno
from Curso import Curso
from Servidor import Servidor
from Coordernador import Coordenador
from Diretor import Diretor

usuario1 = Professor()
curso1 = Curso("Sistemas de Informação")

curso1.adicionarDisciplina("Lógica de Programação")
curso1.adicionarDisciplina("MPOO")
curso1.definirSala("MPOO", "Sala 15")
curso1.listarDisciplinas()

usuario2 = Aluno()
usuario2.verCursosDisponiveis()
usuario2.selecionarCurso(1)
usuario2.mostrarDisciplinas()

usuario3 = Servidor()
usuario4 = Coordenador()
usuario5 = Diretor()
