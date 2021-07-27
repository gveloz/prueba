#creación de la clase
class Persona:
    #método constructor
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def __str__(self):
        return self.nombre
    
    def presentarse(self):
        print("Hola Me llamo {}, ¿Cómo te llamas?".format(self.nombre))

    def responder(self, otro):
        print("Hola {}, me llamo {}".format(otro.nombre, self.nombre))
    
    def preguntar_edad(self, otro):
        print("{}, ¿Cuántos años tienes?".format(otro.nombre))

    def responder_edad(self,otro):
        print("{}, tengo {} años".format(otro.nombre,self.edad))


# Crear los objetos
ojorge = Persona("Jorge", 30)
omaria = Persona("María", 25)


#Uso de Mensaje
# Presentarse entre objetos
omaria.presentarse()
ojorge.responder(omaria)

omaria.preguntar_edad(ojorge)
ojorge.responder_edad(omaria)

