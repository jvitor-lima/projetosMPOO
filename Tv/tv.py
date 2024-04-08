class TV:

    def __init__(self, marca, cor, ano_fabricacao, polegadas, qualidade_imagem):
        self.marca = marca
        self.cor = cor
        self.ano_fabricacao = ano_fabricacao
        self.polegadas = polegadas
        self.qualidade_imagem = qualidade_imagem
        self.power = False
        self.volume = 50
        self.canal = 1
        self.volume_anterior = None
        self.mudo = False

    def Power(self):
        self.power = not self.power
        return self.power

    def Aumentarvolume(self):
        if self.mudo == True:
            self.volume = self.volume_anterior
            self.mudo = False
            print('removido do mudo')
        if self.volume == 100:
            print('o volume está no maximo')
        else:
            self.volume = self.volume + 1
            return self.volume

    def Diminuirvolume(self):
        if self.mudo == True:
            self.volume = self.volume_anterior
            self.mudo = False
            print('removido do mudo')
        if self.volume == 0:
            print('o volume está no minimo')
        else:
            self.volume = self.volume - 1
            return self.volume

    def Proximocanal(self):
        self.canal = self.canal + 1
        return self.canal

    def Canalanterior(self):
        self.canal = self.canal + 1
        return self.canal

    def Mudo(self):
        self.volume_anterior = self.volume
        self.mudo = not self.mudo
        if self.mudo == True:
            self.volume = 0
        else:
            self.volume = self.volume_anterior

        return self.mudo
        # return print('mutado')

    def mudar_canal(self, num):
        self.canal = num
        return self.canal

    def Get_info(self):
        print("Informações da TV")
        print("Marca:", self.marca)
        print("Cor:", self.cor)
        print("Ano de Fabricacao:", self.ano_fabricacao)
        print("Polegadas:", self.polegadas)
        print("Qualidade de Imagem:", self.qualidade_imagem)


controle1 = TV(marca="LG", cor="preta", ano_fabricacao=2024,
               polegadas=55, qualidade_imagem="4K")

print(controle1.Get_info())
print(controle1.Power())
print(controle1.Diminuirvolume())
print(controle1.Proximocanal())
print(controle1.Diminuirvolume())
print(controle1.Mudo())
print(controle1.Aumentarvolume())
print(controle1.mudar_canal(7))
print(controle1.Aumentarvolume())
