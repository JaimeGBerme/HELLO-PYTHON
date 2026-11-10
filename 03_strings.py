#strings
my_string= "mi string"
my_other_string="mi otro string"

print(len(my_string))
print(len(my_other_string))

print (my_string + " " + my_other_string)

my_new_line_string="Este es un texto\ncon salto de linea"
print (my_new_line_string)
my_tab_string="\tEste es un texto\ncon tabulacion y salto de linea"
print (my_tab_string)

#Formateo
name, surname, age ="Jaime","Garcia" ,44
print ("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # en cada {} se mete cada una de las variables del formateo
print ("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # en cada {} se mete cada una de las variables indicada en %(), %s para string, %d para entero

print (f"Mi nombre es {name} {surname} y mi edad es {age}") # importante poner la f antes de la cadena

#desempaqueta de caracteres
language="python"
a, b,c,d,e,f= language #tiene que haber tantos variables como carcteres del contenido de la variable
print(a)

# División

language_slice=language[1:3]#substring. Empieza por 0. Si se omite el segundo parametro es hasta el final
print(language_slice)

language_slice=language[-2]#lee el segundo caracter empezando por el final del string. Empieza por el -1
print(language_slice)

reverse_language=language[::-1]#invierte el orden de los caracteres
print(reverse_language)

#funciones del sistema
print (language.capitalize())#pone en mayusculas el primer caracter

print(language.upper())#pone en mayusculas todos los caracteres de la cadena

print(language.count("t"))#cuenta el numero de veces que parece un caracter (t) en la cadena

print(language.isnumeric())
print("1".isnumeric()) #Devuelve si es numerico o no. Ojo que en este casi devuelve que si a pesar de estar entre comillas

print(language.capitalize().isupper())#Devuelve si TODA la cadaena está en mayusculas. Se ve que se puede unir y ejecutar 2 funciones en una. Las ejecuta en orden de izq a der

print(language.startswith("py"))#Devuelve si la cadena empieza por los caracteres indicados. Es sensible amyusculas