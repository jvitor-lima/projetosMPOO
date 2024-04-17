class Endereco:
    def __init__(self):
        self.rua = ""
        self.numero = ""
        self.bairro = ""
        self.cep = ""
        self.complemento = ""
        self.municipio = ""
        self.estado = ""
        
    def ruaGet(self):
        return self.rua
    
    def bairroGet(self):
        return self.bairro
    
    def municipioGet(self):
        return self.municipio
    
    def estadoGet(self):
        return self.estado
    
    def cepGet(self):
        return self.cep
    
    def cadastrarEndereco(self, rua, numero, bairro, cep, complemento, municipio, estado):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.complemento = complemento
        self.municipio = municipio
        self.estado = estado
        print("Endereço cadastrado com sucesso!")
             
    def listarEndereco(self):
        enderecoCompleto = f"{self.rua} {self.numero} {self.bairro} {self.cep} {self.complemento} {self.municipio} {self.estado}"
        print(enderecoCompleto)
