#lectura fichero
class fichero:
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
#escritura fichero
