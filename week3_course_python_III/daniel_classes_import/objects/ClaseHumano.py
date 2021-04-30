#ten en cuenta que en este archivo SOLO se define la clase, no interactuamos aún con ClaseOrco, eso
#lo harás en el jupyter notebook, por tanto no hace falta que crees la instancia daniel en este .py
#hazlo para probar que funcionan las funciones, pero luego bórralo
#crear esta instancia si será lo primero que tengas que hacer una vez importes la clase al notebook

class Humano(object): # te faltaba para definir la clase los paréntesis al lado de Humano

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
        #x = orco #no consigo que python acepta el parametro para llamar al otro archivo
        # no hace falta que indiques el nombre de la instancia karina, eso lo harás al llamar al método
        # daniel.atacar(karina)
        orco.salud = orco.salud - (self.ataque - orco.armadura)
        print(f'Este Orco {orco.nombre} termina con {orco.salud} puntos de vida.')

    def no_vivo(self): #he quitado la comita de al lado de self... (self,) ¿?
        if self.salud <= 0:
            return True
        else:
            return False

    def actualatr(self):
        return f'Nombre: {self.nombre} | dientes: {self.dientes} | salud: {self.salud} | armadura: {self.armadura} | nivel: {self.nivel} | ataque: {self.ataque} | ojos: {self.ojos} | piernas: {self.piernas} |'
        #he cambiado el print() por return, mejor ;) 

#daniel = Humano(nombre='daniel', armadura=3, nivel=34, ataque=6)



    



     


    
    
    
    
    

#Una función llamada 'atacar' que recibe un argumento 'orco' que representa otra clase ('Orco'). Esta función resta a la vida del 'Orco' el ataque de 'Humano' menos la armadura de 'Orco'. Al final, muestra por pantalla la vida del 'Orco'
#Una función no_vivo que retorna True si la vida del 'Humano' es igual o inferior a 0, False en otro caso.
#Una función que muestre por pantalla todos los atributos actuales de 'Humano' concatenados con un String representando el nombre del atributo que se muestra. Ejemplo: "Nombre: Ataulfo | dientes: 32 | salud: 100 | ...")
