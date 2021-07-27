from ejemploherencia import *

#librerías necesarias limpiar la pantalla
import platform
import os
import time

#función para limpiar pantalla
def limpiar_pantalla():
    time.sleep(2)
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")

#crear objetos de clase persona (clase padre)
oPersona1=Persona("JOSE",20)
print(oPersona1.getNombre())

#crear objetos de la clases hijas
oCliente1=Cliente("PEPE", 30, 3000)
print (oCliente1.getNombre())
print (oCliente1.getPresupuesto())

#crear objetos de la clase hija Socio
oSocio1=Socio("JOSÉ2", 23, 300, 20)
print (oSocio1.beneficio)

#crear objetos de la clase Profesor (herencia múltiple)
oProfesor1=Profesor("Germania Veloz", 41, 300,200)
print ("Presupuesto", oProfesor1.getPresupuesto())

#comentario
condicion=False
while condicion==False:
    limpiar_pantalla()
    print("========MENU============")
    print("1. Presupuesto Cliente")
    print("2. Estado de Socio")
    print("3. Asignatura Profesor")
    print("0. Salir")
    
    opcion=int(input("Introduzca la opción deseada: "))
    if opcion==1:
        print ("El presupuesto del cliente es: ", oCliente1.getPresupuesto())
    elif opcion==2:
	    oSocio1.estadoSocio()
    elif opcion==3:
        print("Nombre del profesor", oProfesor1.getNombre(), "es profesor de: ", oProfesor1.getAsignatura())
    elif opcion==0:
        print ("Adios ...")
        condicion=True
        exit()

