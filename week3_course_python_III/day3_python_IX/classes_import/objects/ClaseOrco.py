class Orco():

    def __init__(self, nombre, armadura, nivel, ataque, ojos=2, piernas=2, dientes=56, salud=100):
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.salud = salud

grufalo = Orco(nombre='grufalo', armadura=15, nivel=50, ataque=40)

print(grufalo.nivel)