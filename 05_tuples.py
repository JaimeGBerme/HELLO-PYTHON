#Tuples: permite menos metodos que las listas. Es inmutable. Una vez que lo creas no permite cambiar los valores ni añadir, ni borrar...

my_tuple=tuple()
my_other_tuuple=()

my_tuple=(44,1.74,"Jaime","García")
print(my_tuple)

my_tuple=list(my_tuple)#podemos convertir la tupla a lista
print(type(my_tuple))
my_tuple.insert(1,"Azul")
print(tuple(my_tuple))#se puede volver a convertir en tupla
del my_tuple  #a pesar de ser inmutable , de puede eliminar la tupla. La variable entera, no vaciarla de valores