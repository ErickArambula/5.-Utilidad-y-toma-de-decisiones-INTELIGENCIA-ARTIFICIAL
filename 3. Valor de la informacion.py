import random

# Función para simular una tirada de una moneda cargada
def tirar_moneda_cargada(probabilidad_cara):
    if random.random() < probabilidad_cara:
        return "Cara"
    else:
        return "Sello"

# Función para calcular el valor esperado de obtener información adicional
def valor_informacion(probabilidad_cara_actual, costo_informacion):
    # Calcula el valor esperado de obtener información adicional (cara o sello) 
    valor_cara = probabilidad_cara_actual * (1 - costo_informacion)
    valor_sello = (1 - probabilidad_cara_actual) * (1 - costo_informacion)
    return valor_cara, valor_sello

# Probabilidad inicial de obtener cara
probabilidad_cara_actual = 0.6

# Costo de obtener información adicional (0 significa que es gratis)
costo_informacion = 0.1

# Tira una moneda cargada para decidir si obtener información adicional
resultado_moneda = tirar_moneda_cargada(probabilidad_cara_actual)

if resultado_moneda == "Cara":
    # Elige obtener información adicional
    valor_cara, valor_sello = valor_informacion(probabilidad_cara_actual, costo_informacion)
    decision = "Obtener información adicional (Cara)"
else:
    # Decide no obtener información adicional
    valor_cara, valor_sello = probabilidad_cara_actual, 1 - probabilidad_cara_actual
    decision = "No obtener información adicional (Sello)"

# Muestra la decisión y los valores esperados
print(f"Decisión: {decision}")
print(f"Valor esperado de obtener Cara: {valor_cara:.2f}")
print(f"Valor esperado de obtener Sello: {valor_sello:.2f}")
