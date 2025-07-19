class Lampada:
    def __init__(self, ligada = False):
        self.ligada = ligada

    def ligar(self):
       if self.ligada:
           return "já está ligada"
       self.ligada = True
       return "ligando a lampada"


    def desligar(self):
        if self.ligada:
            return "já está desligada"
        self.ligada = False
        return " desligando a lampada"
           
rommate = Lampada()
print(rommate.desligar())    