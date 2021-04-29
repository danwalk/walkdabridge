import ClaseOrco as o

class Humano:

    def __init__(self, nombre, armadura, nivel, ataque, ojos=2, piernas=2, dientes=32, salud=100):
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.salud = salud

    def atacar(self, orco):
        x = orco #no consigo que python acepta el parametro para llamar al otro archivo
        o.karina.salud = o.karina.salud - (self.ataque - o.karina.armadura)
        print(f'Este Orco {o.karina.nombre} termina con {o.karina.salud} puntos de vida.')

    def no_vivo(self,):
        if self.salud <= 0:
            return True
        else:
            return False

    def actualatr(self,):
        print(f'Nombre: {self.nombre} | dientes: {self.dientes} | salud: {self.salud} | armadura: {self.armadura} | nivel: {self.nivel} | ataque: {self.ataque} | ojos: {self.ojos} | piernas: {self.piernas} |')

daniel = Humano(nombre='daniel', armadura=3, nivel=34, ataque=6)

    



     


    
    
    
    
    

#Una función llamada 'atacar' que recibe un argumento 'orco' que representa otra clase ('Orco'). Esta función resta a la vida del 'Orco' el ataque de 'Humano' menos la armadura de 'Orco'. Al final, muestra por pantalla la vida del 'Orco'
#Una función no_vivo que retorna True si la vida del 'Humano' es igual o inferior a 0, False en otro caso.
#Una función que muestre por pantalla todos los atributos actuales de 'Humano' concatenados con un String representando el nombre del atributo que se muestra. Ejemplo: "Nombre: Ataulfo | dientes: 32 | salud: 100 | ...")