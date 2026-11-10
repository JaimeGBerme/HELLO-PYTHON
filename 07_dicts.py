#Diccionarios:tipo de estructura que  permite crear clave y su valor. El valor puede ser una lista , un set, una tupla,otro diccionario...
my_dict = dict()
my_other_dict = {}
print (type(my_dict))

my_other_dict = {"Nombre":"Jaime","Apellido":"Garcia","Edad":44,1:"Python"}

my_dict = {
    "Nombre":"Jaime",
    "Apellido":"Garcia",
    "Edad":44,
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.77
    }
print(my_other_dict)
print(my_dict)

print (len(my_other_dict))#cuenta el numero de elementos a nivuel superior del diccionario, no cuenta los elementos que pueda tener uno de sus sub elementos
print (len(my_dict))

print (my_dict["Nombre"])
my_dict["Nombre"]="Superman"
print (my_dict["Nombre"])
print (my_dict[1])

my_dict["Calle"]="Mi calle" # asi se añade un nuevo campo y su valor al diccionario.
print(my_dict)

del my_dict["Calle"]#si le pasamos uno de los elementos del diccionario sólo borra ese. Si no lo pasaramos , borraria todo el diccionario
print(my_dict)

print("Superman" in my_dict)#Se busca por clave , no por valor
print("Eustaquio" in my_dict)
print(my_dict.items())
print(my_dict.keys())#retorna una lista de claves
print(my_dict.values())#retorna una lista de valores incluidos los sets,listas... que pueda contener

my_new_dict=my_other_dict.fromkeys(("Nombre",1,"inventado"))#crea un nuevo diccionario a partir de las claves de otro. Incluso permite añadir otras claves que no estuvieran en el original
print(my_new_dict)
my_new_dict=dict.fromkeys(my_dict)#copiamos la estructura completa de un diccionario a uno nuevo.Ya ser rellenarames los valores cuando deseemos
print(my_new_dict)