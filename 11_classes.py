#classes

class MyEmptyPerson:
    pass #instrucción del sistema para que no de error en funciones y clases

print(MyEmptyPerson)

class Person:
    def __init__(self,name, surname, alias="sin alias") -> None: #constructor de clase
        #propiedades:
        self.__name=name.capitalize()#si se pone "__" delante de la propiedad se convierte en privada y no se puede acceder a ella desde fuera de la clase
        self.__surname=surname.capitalize()
        self.nombre_completo=f"{name.capitalize()} {surname.capitalize()} ({alias.capitalize()})"#Propiedad pública
        self.especie="humano" #este valor no se pasa como parametro , está a fuego en la clase para todas sus instancias

    def get_apellido(self):
        return self.__surname

    def walk(self):
        print(f"{self.nombre_completo} Está camnianado")


my_person=Person(input("Introduzca nombre"),input("Introduzca apellido"))

print(my_person.nombre_completo,my_person.especie)
my_person.walk()

my_person.nombre_completo= "Ejemeeplo para sobre escribir" #despues de crear la clase y asignar sus parámetros, se pueden sobreescrbir
print(my_person.nombre_completo)
#print(my_person.__name) #no se puede acceder a propiedad privada de una clase si no se le crea una funcion, dentro de la misma , que lo devuelva
print(my_person.get_apellido()) #se puede acceder al valor de esta propiedad privada mediante la funcion que hemos creado pero no se puede modificar directamente su valor
#faltan por estudiar herencia y polimorfismo

class Estudiante (Person):
    def __ini__(self):
        self.curso="tercero"
        super().__init__()
    def saludar(self):
        print ("Mi nombre es "+ self.nombre_completo)

my_estudiante=Estudiante("Lucas","Grijander","empollon" )

my_estudiante.saludar()
