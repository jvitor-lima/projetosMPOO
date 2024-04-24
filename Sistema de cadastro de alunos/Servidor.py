from Pessoa import Pessoa


class Servidor(Pessoa):
    idServidor = 0

    def __init__(self):
        self.nome = input("Digite o nome do servidor: ")
        super().__init__()
        Servidor.idServidor += 1
        self.idServidor = f"S{Servidor.idServidor:04d}"
        print(f"Nome: {self.nome}\nID Servidor: {self.idServidor}")
        print("Servidor cadastrado com sucesso!")
