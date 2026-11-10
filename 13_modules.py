#modules: Una especie de libreria. Un lugar externo donde almacenar el codigo

import my_module #Se puede importa todo un modulo
from   my_module import sumvalores, imprimir # o importar sólo parte del modulo para no ocupar mucha memoria
import math
print(math.pi)
print (math.pow(2,16))
import random
from math import pi as PI_VALUE
print(PI_VALUE)





my_module.sumvalores(1,2,3)
my_module.imprimir("Hola")
