class TV:

    def __init__(self):
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
            print('removido do mudo')

        if self.volume == 100:
            print('o volume está no maximo')
        else:
            self.volume = self.volume + 1
            return self.volume

    def Diminuirvolume(self):
        if self.mudo == True:
            self.volume = self.volume_anterior
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


controle1 = TV()
print(controle1.Power())
print(controle1.Diminuirvolume())
print(controle1.Diminuirvolume())
print(controle1.Mudo())
print(controle1.Aumentarvolume())
