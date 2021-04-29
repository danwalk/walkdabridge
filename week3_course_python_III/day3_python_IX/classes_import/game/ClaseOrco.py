import ClaseHumano as h

class Orco:

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
        x = orco #no consigo que python acepta el parametro para llamar al otro archivo
        h.daniel.salud = h.daniel.salud - (self.ataque - h.daniel.armadura)
        print(f'Este Humano {h.daniel.nombre} termina con {h.daniel.salud} puntos de vida.')

    def no_vivo(self,):
        if self.salud <= 0:
            return True
        else:
            return False
    
    def actualatr(self,):
        print(f'Nombre: {self.nombre} | dientes: {self.dientes} | salud: {self.salud} | armadura: {self.armadura} | nivel: {self.nivel} | ataque: {self.ataque} | ojos: {self.ojos} | piernas: {self.piernas} |')

karina = Orco(nombre='karina', armadura=2, nivel=30, ataque=5)



