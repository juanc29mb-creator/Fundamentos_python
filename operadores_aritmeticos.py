from operator import mul
import re


a=3
b=2

#suma
suma=a+b
print(f"La suma de {a} y {b} es: {suma}")

#resta
resta=a-b   
print(f"La resta de {a} y {b} es: {resta}")

multiplicacion=a*b
print(f"La multiplicacion de {a} y {b} es: {multiplicacion}")   

divicion=a/b
print(f"La divicion de {a} y {b} es: {divicion}")       

modulo = a%b
print(f"El modulo de {a} y {b} es: {modulo}")           

divicion_entera=a//b
print(f"La divicion entera de {a} y {b} es: {divicion_entera}")     

potencia=a**b
print(f"La potencia de {a} y {b} es: {potencia}")       

#precedencia de operadores
resultado= a + b * 2    
print(f"El resultado de la operacion es {a} + {b} * 2: {resultado}")   

resultado= (a + b) * 2
print(f"El resultado de la operacion es ({a} + {b}) * 2: {resultado}")      

resultado= a*b//3
print(f"El resultado de la operacion es {a} * {b} // 3: {resultado}")       

resultado=(a + b)//3
print(f"El resultado de la operacion es ({a} + {b}) // 3: {resultado}")

resultado= a*(b//3)
print(f"El resultado de la operacion es {a} * ({b} // 2): {resultado}")

ejercicio= 3 + 4 * 2 / (1 - 5) ** 2 ** 3


ejercicio=((a+b)*(a-b))/(a*b)


import math

print(math.pi)
print(math.sqrt(16))    
print(math.e)

import random   

random.random
numero_aleatorio=random.random(1,10)
print(numero_aleatorio)