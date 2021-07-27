from ClasesHerencia import *

#Creación de objetos Persona
oPersona1=Persona("JOSÉ", 40)
print(oPersona1.getNombre())
print(oPersona1.getEdad())

#Crear objetos de las clases hijas
oCliente1=Cliente("ANA", 40, 3000)
print(oCliente1.getNombre())
print(oCliente1.getPresupuesto())

#Crear objetos de Empleado

oEmpleado1=Empleado("Inés", 20, 580)
print("La edad del empleado es: ",oEmpleado1.getEdad())

#Crear objeto de clase Socio
oSocio1=Socio("FELIPE",20,3000,500)
oSocio1.estadoSocio()
print(oSocio1.getPresupuesto())

#Crear objeto de Profesor
oProfesor1=Profesor("Germania", 41, 1500,300, "asignatura")
print(oProfesor1.getSalario())