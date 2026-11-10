#conditionals
my_condition = False
if my_condition ==False:# Es lo mismo que if my_condition ==True:
    print ("Se ejecuta la condicion del if")

my_condition = 5*5
if my_condition ==10:# Es lo mismo que if my_condition ==True:
    print ("Se ejecuta la condicion del segundo if")

if my_condition >10 and my_condition<20:
    print ("Es mayor que 10 y menor que 20")
elif my_condition==25:#las condiciones se evaluan en el orden que están escritas
    print ("Es igual a 25")
else:
    print ("Es menor o igual que 10 o mayor o igual que 20")
    print ("Segundo texto del else")

print ("La ejecucion continua")

my_string = "Mi cadena de texto"
if  my_string or 1==2:
    print("Mi cadena de texto no es vacia")
if my_string == "Mi cadena de textooooooo":
    print("Estas cadenas de texto coinciden")
