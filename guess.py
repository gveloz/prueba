class Empleado: 
     def __init__(self): 
          self._edad = 0
       
     # using property decorator 
     # a getter function 
     @property
     def edad(self): 
         print("Se llamo el metodo getter") 
         return self._edad
       
     # a setter function 
     @edad.setter 
     def edad(self, a): 
         if(a < 18): 
            raise ValueError("No es mayor de edad") 
         print("Se llamo el metodo setter") 
         self._edad = a 
  
mark = Empleado() 
  
mark.edad = 19
print(mark.edad)