#functions: intentan resolver un problema concreto de forma centralizado




def my_function ():
    print("esto es una función")


for elemento in (1,2,3):
    print(elemento)
    my_function ()


def sum_two_values(firs_value, second_value): #first_number: int--> se puede poner un tipado de los parametros pero no vale para nada porque luego puedes pasar lo que quieras
    return firs_value+ second_value

print(sum_two_values(3,2))
for elemento in (10,2,7):
    print(sum_two_values(2,elemento))
    
def print_name(name,surname):
    print(f"{name} {surname}")

print_name (surname="García",name="jaime")# se puede cambiar el orden de los paramentros que se pasan a la función si se especifica en la llamada

def print_name_with_default(name,surname,alias = ""):#Parametros opcionales con "=", si se pasa valor lo tomara , si no, el indicado después del "=". Todos los parámetros opcionales tienen que estar a la derecha de la función
    print(f"{name} {surname} {alias}")

print_name_with_default ("jaime","García","JGB")
print_name_with_default ("jaime","García")

def print_texts(*text,cuantos :int=2):#el asterisco en el parámetro text indica que se pueden pasar infinitos parametros. El parametro de la derecha no falla pero no se como pasarlo en la llamada
    print (text)

print_texts("Hola")
print_texts("Hola","Adios","kk")

#funcion que recoge en **kwargs un diccionario para crear una select a BBDD
def filter(**kwargs):
    query = "SELECT * FROM clientes"
    i = 0
    for key, value in kwargs.items():
        if i == 0:
            query += " WHERE "
        else:
            query += " AND "
        query += "{}='{}'".format(key, value)
        i += 1
    query += ";"
    return query

print(filter())
print(filter(ciudad="Madrid"))
print(filter(ciudad="Madrid",fecha_alta="25-10-2018"))