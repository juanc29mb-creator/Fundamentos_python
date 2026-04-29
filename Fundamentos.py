#Variables
nombre="Juan Carlos"
apellidos="Merchan Ballesters"
edad= 20
altuara= 1.80
activo= True
correo="juanc29mb@gmail.com"
telefono= "123456789"
cedula=1858352061

#costeo: convercion tipo de datos
telefono_int=int(telefono)
edad_float=float(edad)
altuara_int=int(altuara)
cedula_str=str(cedula)  

#imprimir tipo de variables
print(type(nombre),nombre)
print(type(apellidos),apellidos)
print(type(edad),edad)
print(type(altuara),altuara)
print(type(activo),activo)
print(type(correo),correo)
print(type(telefono),telefono)
print(type(cedula),cedula)

print(type(telefono_int),telefono_int)
print(type(edad_float),edad_float)
print(type(altuara_int),altuara_int)
print(type(cedula_str),cedula_str)     


#identacion de python

if 5 > 2:
    print("5 es mayor que 2")

else:
    print("5 no es mayor que 2")        

#Iputs
nombre_completo=input("Ingrese su nombre completo: ")
print(nombre_completo)

edad=int(input("Ingrese su edad: ") )
print(type(edad),edad) 

#imprimir con formato f-string
print(f"Hola {nombre_completo}, tienes {edad} años.")
