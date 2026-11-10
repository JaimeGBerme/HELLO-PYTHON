#loops

#while
my_condition = 0
while my_condition<10:
    print(my_condition)
    my_condition+=2
else:#eso no lo tienen todos los mensajes. Permite ejecutar algo justo cuando empieza a no cumplir la condicion
    print("mi condicion es mayor o igual que 10")



while my_condition<20:
    my_condition+=1
    if my_condition==15:
        print("Mi condicion es 15")    
        break # para salir del bucle
    print("Mi condicion es", my_condition)

print ("la ejecución continua")
#for
my_list=[35,24,62,52,30,30,17]
for element in my_list:# tambien se puede poner directamente la lista aqui, en vez de la variable: [10,24,62,52,30,30,17]
    print (element)
my_tuple= (35,1.74,"Jaime","García","JGB")
for element in my_tuple:
    print (element)
my_set={"Jaime","García",44}
for element in my_set:
    print (element)
my_dict= {"Nombre":"Jaime","Apellido":"García","Edad":44,1:"Prueba"}
for mi_variable_elementos in my_dict:
    print (mi_variable_elementos)
    if mi_variable_elementos=="Edad":
        #print("Hemos salido")
        #break
        continue#no recomendado; es equivalente a los GOTO de lenguajes antiguos
    print ("No se lo ha saltado")
else:
    print("El bucle for para el diccionario ha finalizado")