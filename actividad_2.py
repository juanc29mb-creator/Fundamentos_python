# ACTIVIDAD 2: CALCULADORA DE NOTAS

print("--- SISTEMA DE CALIFICACIONES ---")

# 1. Solicitar las tres notas
nota1 = float(input("Ingrese la nota del primer parcial: "))
nota2 = float(input("Ingrese la nota del segundo parcial: "))
nota3 = float(input("Ingrese la nota del tercer parcial: "))

# 2. Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3

# 3. Calcular cuánto falta para la nota máxima (5.0)
puntos_faltantes = 5.0 - promedio

# 4. Determinar si aprueba (promedio >= 3.0)
aprobado = promedio >= 3.0

# 5. Mostrar resultados usando round() y formato legible
print("\n" + "="*30)
print(f"RESUMEN DE NOTAS")
print("="*30)

# Aquí usamos round(variable, decimales)
print(f"Promedio Final:     {round(promedio, 2)}")
print(f"Puntos para el 5.0: {round(puntos_faltantes, 2)}")

# Usamos un if simple para mostrar un mensaje de texto según el booleano
if aprobado:
    print("Estado:             ✅ APROBADO")
else:
    print("Estado:             ❌ REPROBADO")

print("="*30)
