#listas
my_list=list()
my_other_list=[]

print (len(my_list))

my_list=[35,24,62,52,30,30,17]

print(my_list)#cuenta el numero de elementos de la lista
print (len(my_list))#cuenta el numero de elementos de la lista
my_other_list=[44,1.74,"Jaime","García"]
print(my_other_list[0])#accedemos al primer elemento de la lista
print(my_other_list[-1])#accedemos al último elelmnto de la lista

print(my_list.count(30))#cuenta el numero de veces que aparece un valor , en este caso 30, en la lista

age,height,name ,surname=my_other_list#se puede asignar todos los valores de la lista a diferentes variables. Es obligatorio desempaquetar en tantas variables como elementos tenga la lista
print (name)

print(my_list+my_other_list)#concatenar 2 listas
my_other_list.append("JGB")#Añade al final
print (my_other_list)
my_other_list[1]="JGF"#se puede modificar el valor de un elemento de una lista
my_other_list.insert(1,"texto insertado")#inserta en la posicion indicada en el primer parametro
print (my_other_list)
my_other_list.remove("texto insertado")#elimina el primero elmento (solo uno) de la lista que coincida con el texto indicado
print (my_other_list)

print(my_list.pop())#elimina el ultimo elemento  de la lista. adicionalmente devuelve el valor de ese lemento eliminado
print(my_list)
my_pop_element=my_list.pop(2)#Se puede eliminar el elemento indica por indice
print(my_pop_element)
del my_list[2] #eliminamos, sin retornar, el elemento indicado de la lista
my_new_list=my_list.copy()#copia una lista en otra
my_list.clear()#borramos la lista completa
print(my_list)
print(my_new_list)
my_new_list.reverse()#invierte el orden de los elementos de la lista
print(my_new_list)
my_new_list.sort()#ordena la lista. Permite que se le pasen criterios de ordenacion
print(my_new_list)
print(my_new_list[1:3])#se puede trabajar con rangos de la lista. Comienzo y final