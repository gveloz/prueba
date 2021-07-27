class Persona(object):
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def getNombre(self):
        return (self.nombre)

    def getEdad(self):
        return (self.nombre)   
    
    def setNombre(self, nombren):
       self.nombre=nombren
    
    def setEdad(self, edadn):
       self.edad=edadn

class Cliente(Persona):
    def __init__(self,nombre,edad,presupuesto):
        Persona.__init__(self,nombre,edad)
        self.presupuesto=presupuesto
    
    def getPresupuesto(self):
        return (self.presupuesto)
    
    def setNombre(self, presupueston):
       self.presupuesto=presupueston

oPersona1=Persona("PEPE", 20)

print (oPersona1.getNombre())

oCliente1=Cliente("ANA", 20, 2000)
print (oCliente1.getNombre())
print (oCliente1.getPresupuesto())

