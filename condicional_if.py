# condicional if-elif-else
import string


if False:
    print("la primera condicion es verdadera")

elif False:
    print("la segunda condicion es verdadera en elif")

elif False:
    print("la segunda condicion es verdadera en elif")

else:
    print("la condicion es falsa")


# Ejercicio: clasificacion de edad 
edad= 21

if edad<18:
    print("eres menor de edad")

elif edad>=18 and edad<65:
    print("eres un adulto")

else:
    print("eres un adudlto")


  
# Ejercicio: clasificacion de edad if anidado
 
edad= 12

 
if edad<18:
    if edad>12 and edad<18:
         print("adolesente")
    else:
          print("niño")

else:
    if edad>=18 and edad<60:
        print("adulto")
    else:
        print("eres un adultyto mayor")  

#  operador ternario   

edad=int(input("INGRESE el valor"))
numero=4
if numero % 2 ==0:
    print("el numeroes par")
else:
    print("el numero es impar")

print ("el numero es par if ")