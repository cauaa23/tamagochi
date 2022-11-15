class Tamagotchi:

    def _init_(self, energiaMax: int, saciedadeMax: int, limpezaMax: int, idadeMax: int ):
        self.energiaMax = energiaMax
        self.saciedadeMax = saciedadeMax
        self.limpezaMax = limpezaMax
        self.idadeMax = idadeMax
        self.energia = energiaMax
        self.saciedade = saciedadeMax
        self.limpeza = limpezaMax
        self.idade = 0
        self.diamantes = 0
        self.vivo = True

    def getEnergiaMax(self):
        return self.energiaMax

    def getSaciedadeMax(self):
        return self.saciedadeMax

    def getLimpezaMax(self):
        return self.limpezaMax

    def getIdadeMax(self):
        return self.idadeMax

    def getEnergiaAtual(self):
        return self.energia

    def getSaciedadeAtual(self):
        return self.saciedade

    def getLimpezaAtual(self):
        return self.limpeza

    def getIdadeAtual(self):
        return self.idade

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        return self.vivo

    def brincar(self):
        if self.vivo:
            self.energia -= 2
            self.saciedade -= 1
            self.limpeza -= 3
            self.diamantes += 1
            self.idade += 1
            if self.limpeza <= 0 or self.saciedade <= 0 or self.energia <= 0 or self.idade == self.idadeMax:
                if self.limpeza < 0:
                    self.limpeza = 0
                if self.saciedade < 0:
                    self.saciedade = 0
                if self.energia < 0:
                    self.energia = 0
                self.vivo = False
            return True
        else:
            return False


    def comer(self):
        if self.vivo:
            self.energia -= 1
            if self.saciedade+4 <= self.saciedadeMax:
                self.saciedade += 4
            else:
                self.saciedade = self.saciedadeMax
            self.limpeza -= 2
            self.idade += 1
            if self.limpeza <= 0 or self.saciedade <= 0 or self.energia <= 0 or self.idade == self.idadeMax:
                if self.limpeza < 0:
                    self.limpeza = 0
                if self.saciedade < 0:
                    self.saciedade = 0
                if self.energia < 0:
                    self.energia = 0
                self.vivo = False
            return True
        else:
            return False

    def dormir(self):
        if self.vivo and self.energia <= self.energiaMax-5:
            self.saciedade -= 2
            self.idade += self.energiaMax - self.energia
            self.energia = self.energiaMax
            if self.limpeza <= 0 or self.saciedade <= 0 or self.energia <= 0 or self.idade == self.idadeMax:
                if self.limpeza < 0:
                    self.limpeza = 0
                if self.saciedade < 0:
                    self.saciedade = 0
                if self.energia < 0:
                    self.energia = 0
                self.vivo = False
            return True
        else:
            return False

    def banhar(self):
        if self.vivo:
            self.saciedade -= 1
            self.idade += 2
            self.energia -= 3
            self.limpeza = self.limpezaMax
            if self.limpeza <= 0 or self.saciedade <= 0 or self.energia <= 0 or self.idade >= self.idadeMax:
                if self.limpeza < 0:
                    self.limpeza = 0
                if self.saciedade < 0:
                    self.saciedade = 0
                if self.energia < 0:
                    self.energia = 0
                if self.idade > self.idadeMax:
                    self.idade = self.idadeMax
                self.vivo = False
            return True
        else:
            return False
