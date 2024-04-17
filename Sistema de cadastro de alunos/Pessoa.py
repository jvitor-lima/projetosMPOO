from Endereco import Endereco

class Pessoa:
    def __init__(self):
        self.nome = input("Digite o nome: ")
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
