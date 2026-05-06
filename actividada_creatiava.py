# CALCULADORA DE NÓMINA BÁSICA (COLOMBIA)

#  
SMLV = 1800000  # Salario Mínimo Legal Vigente
AUX_TRANSPORTE = 200000  # Auxilio de Transporte para 2025

# 2. Pedimos la información al usuario
nombre = input("Ingrese el nombre del empleado: ")
salario_base = (input("Ingrese el salario mensual base: "))


# Borramos los puntos o comas que el usuario haya puesto
entrada_limpia = salario_base.replace(".", "").replace(",", "")
# Ahora sí lo convertimos a número
salario_base = float(entrada_limpia)

# 3. Lógica del Auxilio de Transporte
# Se paga si el salario es menor o igual a 2 salarios mínimos
if salario_base <= (SMLV * 2):
    auxilio_pagar = AUX_TRANSPORTE
else:
    auxilio_pagar = 0

# 4. Cálculo de Deducciones (Salud y Pensión)
descuento_salud = salario_base * 0.04
descuento_pension = salario_base * 0.04

# 5. Cálculo del Total Neto a Pagar
total_pagar = salario_base + auxilio_pagar - descuento_salud - descuento_pension

# 6. Mostrar los resultados (El "Recibo")
print("\n" + "="*30)
print(f"RESUMEN DE NÓMINA PARA: {nombre}")
print("="*30)
print(f"Salario Base:        ${salario_base:,.0f}")
print(f"Auxilio Transporte:  ${auxilio_pagar:,.0f}")
print(f"Descuento Salud:    -${descuento_salud:,.0f}")
print(f"Descuento Pensión:  -${descuento_pension:,.0f}")
print("-" * 30)
print(f"NETO A PAGAR:        ${total_pagar:,.0f}")
print("="*30)