#sets : Es como una lista pero sin orden. Por eso mismo , no se puede acceder a sus elementos por indice. Tampoco almacena repetidos.

my_set=set ()
my_other_set ={}#otra forma de crear un set
print (type(my_set))
print(type(my_other_set))#Al definirlo, lo crea como diccionario ¿?¿?¿?
my_other_set ={"Jaime","García",44}
print(type(my_other_set))#al meterle valores ya se convierte en un set

print(len (my_other_set))#nos devuelve el número de elementos del set
#print(my_other_set(2))

my_other_set.add("JGB")
print(my_other_set)#Un set no es una estructura ordenada. 
my_other_set.add("JGB")
print(my_other_set)#A pesar de volver a añadir otra vez el mismo valor, solo se qued con uno de ellos. Un set no admite repetidos

#Para comprobar si un elemento existe en un set:
print ("Jaime" in my_other_set)
print ("jaimo" in my_other_set)

my_other_set.remove(44)
print(my_other_set)
my_set={"Jaime","García",44}
my_list=list(my_set)
print(my_list)
print(my_list[0])

my_new_set=my_set.union(my_other_set)#para unir 2 elementos
print(my_new_set)
print(my_new_set.difference(my_set))