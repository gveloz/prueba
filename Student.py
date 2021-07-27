class Student:
  #métodos
  def __init__(self, matricula, nombre, telefono, edad):
    self.__matricula=matricula
    self.__nombre=nombre
    self.__telefono=telefono
    self.__edad=edad

  def getMatricula(self):
    return self.__matricula

  def getNombre(self):
    return self.__nombre

  def getTelefono(self):
    return self.telefono

  def getEdad(self):
    return self.edad

  def setNombre(self, nuevoNombre):
     self.__nombre=nuevoNombre

  def setMatricula(self, nuevaMatricula):
    self.__matricula=nuevaMatricula

#crear al objeto
oEstudiante=Student("M001", "Ana Luna", "0992987654",  20)  #método constructor
nombree=oEstudiante.getNombre()
print (oEstudiante.getNombre())

oEstudiante.setNombre("María")
print (oEstudiante.getNombre())