# ACTIVIDAD 3: CLASIFICADOR DE IMC (Índice de Masa Corporal)

print("--- BIENVENIDO AL CLASIFICADOR DE IMC ---")

# 1. Solicitar datos al usuario
peso = float(input("Ingrese su peso en kilogramos (kg): "))
estatura = float(input("Ingrese su estatura en metros (m): "))

# 5. Bonus: Validación de valores positivos
if peso > 0 and estatura > 0:
    
    # 2. Calcular el IMC
    imc = peso / (estatura ** 2)

    # 3. Clasificar el resultado usando if / elif / else
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif 18.5 <= imc <= 24.9:
        clasificacion = "Normal"
    elif 25 <= imc <= 29.9:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    # 4. Imprimir resultados
    # Usamos :.2f para mostrar solo 2 decimales
    print("\n" + "="*30)
    print(f"VALOR DE SU IMC: {imc:.2f}")
    print(f"CLASIFICACIÓN:   {clasificacion}")
    print("="*30)

else:
    # Si el usuario puso un número negativo o cero
    print("\nError: El peso y la estatura deben ser valores positivos.")
