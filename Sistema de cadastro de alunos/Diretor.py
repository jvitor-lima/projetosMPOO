from Pessoa import Pessoa


class Diretor(Pessoa):
    idDiretor = 0

    def __init__(self):
        self.nome = input("Digite o nome do diretor: ")
        super().__init__()
        Diretor.idDiretor += 1
        self.idDiretor = f"D{Diretor.idDiretor:04d}"
        print(f"Nome: {self.nome}\nID Diretor: {self.idDiretor}")
        print("Diretor cadastrado com sucesso!")
