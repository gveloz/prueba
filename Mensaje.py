class Persona:
    
    def __init__(self, nombre, edad): 
         self.nombre =nombre
         self.edad=edad
    
    def __str__(self):
       return self.nombre
    
    def presentarse(self):
        print ("Me llamo {}, ¿Cómo te llamas?".format(self.nombre))
    
    def responder(self, otro):
        print("Hola {}, me llamo {}.".format(otro.nombre, self.nombre))
    
    def preguntar_edad(self, otro):
        print ("Hola {}, ¿cuántos años tiene?".format(otro.nombre))
    
    def responder_edad(self, otro):
        print ("Hola {}, tengo {}años.".format(otro.nombre, self.edad))

ojorge = Persona("Jorge",23)
omaria=Persona("María", 24)

# Saludar y preguntar
ojorge.presentarse()
omaria.responder(omaria) 

# Preguntar edad
#ojorge.preguntar_edad(omaria)
#omaria.responder_edad(ojorge)
