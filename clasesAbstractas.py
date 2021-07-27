from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def saludar (self):
        pass

class Empleado(Persona):
    def __init__(self, cargo):
        self.cargo=cargo

    def saludar(self):
        return "Bienvenido a..."
    
    def correr(self):
        return "Método correr de Empleado"

class Cliente(Persona):
    def __init__(self, direccion):
        self.direccion=direccion
    
    def correr(self):
        return "Método correr de Cliente"
    
    def saludar (self):
        return"Hola...."

e=Empleado("Gerente")
print (e.saludar())
print (e.correr())
c=Cliente("Jose")
print (c.saludar())
print (c.correr())

