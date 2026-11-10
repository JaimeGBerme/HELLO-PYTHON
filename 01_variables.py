#Variables
my_str_variable="Mi variable string"
print(my_str_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#concatenaciond de variables en un print. Hace una conversión de tipos automática
print(my_str_variable,my_int_variable,my_bool_variable)
print("Este es el valor de print my_bool_variable: ",my_bool_variable)

#Algunas funciones del sistema
print(len(my_str_variable))

#variables creadas en una sola línea
name, surname, alias, edad ="Jaime","García Bermejo","Jimmy",44

print("Mi nombre es :",name, surname, "(",alias,")", ". Tengo ",edad, " años")

nombre_jugador=input("¿Cuál es tu nombre? ")
dificultad: int=int(input("¿Qué nivel (1 a 3) de dificultad quieres? "))#cuidado que no se está controlando que el usuario meta un número
print (nombre_jugador) 
print (type(dificultad)) 

#se puede cambiar el tipo de una variable. Esto es peligroso porque puede inducir a errores por ejemplo en proyectos grandes y/o colaborativos
#nombre_jugador=dificultad
nombre_jugador=1
dificultad="mucha"
print ("El nombre ahora vale: ",nombre_jugador, "Con tipo ", str(type(nombre_jugador) ),"La dificultad ahora vale: ", dificultad, "con tipo ", str(type(dificultad) )) 

#Declaracion del tipo de una variable pero no se bloquea el tipo por lo que se puede seguir cambiando ...
direccion : str="Hatshepsut"
