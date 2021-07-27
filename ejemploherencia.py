#creando la clase PADRE
class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    #MÉTODOS GET Y SET
    def getNombre(self):
        return(self.nombre)
    
    def getEdad(self):
        return (self.edad)
    
    def setNombre(self, nombren):
        self.nombre=nombren

    def setEdad(self, edadn):
        self.edad=edadn

#crear la clase hija
class Cliente(Persona):
    def __init__(self, nombre, edad, presupuesto):
        Persona.__init__(self, nombre, edad)
        self.presupuesto=presupuesto
    
    def getPresupuesto(self):
        return (self.presupuesto)
    
    def setPresupuesto(self, presupueston):
        self.presupuesto=presupueston

#crear la clase hija
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        Persona.__init__(self, nombre, edad)
        self.salario=salario
    
    def getSalario(self):
        return (self.salario)
    
    def setSalario(self, salarion):
        self.salario=salarion
        

class Socio(Cliente):
    def __init__(self, nombre, edad, presupuesto, beneficio):
        super().__init__(nombre, edad, presupuesto)
        self.beneficio=beneficio
    
    def getBeneficio(self):
        return (self.beneficio)
    
    def setBeneficio(self, presupueston):
        self.beneficio=presupueston

    def estadoSocio(self):
        if self.beneficio>100:
            print ("Socio Factible")
        else:
            print ("Socio No Sustentable")

 #Herencia múltiple
class Profesor(Empleado,Cliente):
     def __init__(self, nombre, edad, salario, presupuesto):
         super().__init__(nombre, edad, salario)
         self.asignatura=input("Ingrese la asignatura: ")
         self.presupuesto=presupuesto
    
     def getAsignatura(self):
         return(self.asignatura)
    
     def setAsignatura(self,asignatura):
         self.asignatura=asignatura