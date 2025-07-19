class Relogio:
    def __init__(self,horas,minutos):
        self.horas = horas
        self.minutos = minutos
    
    def mostrar_hora(self):
        return f"agora são {self.horas}:{self.minutos}"

pessoa_que_ve_a_hora = Relogio(10,15)
print(pessoa_que_ve_a_hora.mostrar_hora())