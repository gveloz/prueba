class Perro:
    def hablar(self):
        print("Guau,Guau!!")

class Gato:
    def hablar(self):
        print("Miau,Miau")

class Vaca:
    def hablar(self):
        print("MUUU, MUUU!!")

def llama_hablar(x):
    x.hablar()

mascota1=Perro()
mascota2=Gato()
mascota3=Vaca()
mascota=Perro()
llama_hablar(mascota3)

TestArray=[]
TestArray.append(mascota1)
TestArray.append(mascota2)
llama_hablar(TestArray[0])


