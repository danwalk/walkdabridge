# este archivo es un espejo de ClaseHumano, revisa antes ese archivo que te he explicado un par de cositas
class Orco(object):

    def __init__(self, nombre, armadura, nivel, ataque, ojos=2, piernas=2, dientes=56, salud=100):
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.salud = salud

    def atacar(self, human):
        #x = orco NOP
        human.salud = human.salud - (self.ataque - human.armadura)
        print(f'Este Humano {human.nombre} termina con {human.salud} puntos de vida.')

    def no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False
    
    def actualatr(self):
        return f'Nombre: {self.nombre} | dientes: {self.dientes} | salud: {self.salud} | armadura: {self.armadura} | nivel: {self.nivel} | ataque: {self.ataque} | ojos: {self.ojos} | piernas: {self.piernas} |'

#karina = Orco(nombre='karina', armadura=2, nivel=30, ataque=5)

