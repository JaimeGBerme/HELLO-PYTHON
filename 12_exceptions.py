#exceptions
#MMException handling: Manejo de errores

#try
#print(5+"5")
#else
#finally
numberOne=5
numberTwo=1
numberTwo="1"

#try except
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")#esta línea no se ejecuta si la línea de arriba no ha dado error
except:
    print("Se ha producido un error")

#try except else finally
try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")#esta línea no se ejecuta si la línea de arriba no ha dado error
except:
    print("Se ha producido un error")
else: #se ejecuta si no se produce una excepción. Esta parte es opcional
    print("La ejecución continua")
finally:#Esta parte se ejecuta siempre, de error o no. Esta parte es opcional
    print ("La ejecución continua por el finally")

# excepciones por tipo de error

try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")#esta línea no se ejecuta si la línea de arriba no ha dado error
except ValueError:
    print("Se ha producido un error por Valor de dato")
except TypeError: #Al especificar el tipo de error, esta parte se ejecuta sólo si da ese tipo de error
    print("Se ha producido un error por Tipo de dato")

# Caputa de la información de la excepción

try:
    print(numberOne+numberTwo)
    print("No se ha producido un error")#esta línea no se ejecuta si la línea de arriba no ha dado error
except ValueError as errorJaime:
    print(f"{errorJaime} : Error de Valor")
except TypeError as errorJaime:#error es una variabile, que puede tener ese nombre o cualquier otro, para caputar la información del error
    print(f"{errorJaime} : Error de tipo")

