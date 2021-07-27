#crear la clase Padre
class Persona:
    # método constructor
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    #métodos get y set (ENCAPSULAMIENTO)
    def getNombre(self):
        return(self.nombre)
    
    def getEdad(self):
        return(self.edad)
    
    def setNombre(self,nombren):
        self.nombre=nombren
    
    def setEdad(self,edadn):
        self.edad=edadn

#Crear la clase hija Cliente
class Cliente(Persona):
    def __init__(self, nombre, edad, presupuesto):
        Persona.__init__(self, nombre, edad)
        self.presupuesto=presupuesto
    
    def getPresupuesto(self):
        return(self.presupuesto)
    
    def setPresupuesto(self, presupueston):
        self.presupuesto=presupueston

#Crear clase hija empleado
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario=salario
    
    def getSalario(self):
        return(self.salario)
    
    def setSalario(self, salarion):
        self.salario=salarion

#Crear la clase Socio
class Socio(Cliente):
    def __init__(self, nombre, edad, presupuesto,beneficio):
        super().__init__(nombre, edad, presupuesto)
        self.beneficio=beneficio
    
    def getBeneficio(self):
        return (self.beneficio)
    
    def setBeneficio(self, beneficion):
        self.beneficio=beneficion
    
    def estadoSocio(self):
        if self.getBeneficio()>100:
            print ("Socio Factible")
        else:
            print("Socio No Sustentable")

#Crear clase Profesor (HERENCIA MÚLTIPLE)
class Profesor(Cliente,Empleado):
    def __init__(self, nombre, edad, presupuesto,salario, asignatura):
        super().__init__(nombre, edad, presupuesto)
        self.salario=salario
        self.asignatura=asignatura
          
    def getAsignatura(self):
        return(self.asignatura)
    
    def setAsignatura(self, asignaturan):
        self.asignatura=asignaturan
    
















    












