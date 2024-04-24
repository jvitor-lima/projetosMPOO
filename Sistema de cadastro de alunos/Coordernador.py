from Pessoa import Pessoa


class Coordenador(Pessoa):
    idCoordenador = 0

    def __init__(self):
        self.nome = input("Digite o nome do coordenador: ")
        super().__init__()
        Coordenador.idCoordenador += 1
        self.idCoordenador = f"C{Coordenador.idCoordenador:04d}"
        print(f"Nome: {self.nome}\nID Coordenador: {self.idCoordenador}")
        print("Coordenador cadastrado com sucesso!")
