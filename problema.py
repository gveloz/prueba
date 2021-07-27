[15:50] ANGEL ALBERTO ORTEGA NAVARRETE
#creacion de la clase
class Persona:    
#metodo constructor    
def __init__(self,nombre,edad):
            self.nombre=nombre        
            self.edad=edad    
            
def __str__(self):        
    return self.nombre        
    
def presentarse(self):        
    print("Hola me llamo{​​}​​, como te llmas?".format(self.nombre))    

def responder(self,otro):        
    print("un gusto {​​}​​, me llamo {​​}​​".format(otro.nombre, self.nombre))    

def preguntar_edad(self, otro):        
    print("{​​}​​ cuantos años tienes? ".format(otro.nombre))    

def responder_edad(self,otro):        
    print("Holas {​​}​​, tengo {​​}​​ años".format(otro.nombre, self.edad))
    
#crear los objetos 
opersona1=Persona("Pedro",45) 
opersona2=Persona("juliana",30) 

#uso de mensajes #Que se prensente los objetos
opersona2.presentarse()
opersona1.responder(opersona2)
opersona1.preguntar_edad(opersona2)
opersona2.responder_edad(opersona1)

