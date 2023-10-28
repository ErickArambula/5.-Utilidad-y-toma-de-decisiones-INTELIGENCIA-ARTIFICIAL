# Definición de estados y recompensas
estados = ["S", "A", "B", "C", "T"]  # S: Estado inicial, T: Estado terminal
recompensas = {"S": 0, "A": -1, "B": -1, "C": 10, "T": 0}

# Inicialización de valores de utilidad
valores_utilidad = {estado: 0 for estado in estados}

# Hiperparámetro de descuento
descuento = 0.9

# Algoritmo de iteración de valores
for _ in range(100):
    for estado in estados:
        if estado not in ["S", "T"]:
            mejor_utilidad = max(recompensas[estado] + descuento * valores_utilidad[estado_siguiente]
                                 for estado_siguiente in estados)
            valores_utilidad[estado] = mejor_utilidad

# Mostrar los valores de utilidad finales
for estado, utilidad in valores_utilidad.items():
    print(f"Valor de utilidad de {estado}: {utilidad:.2f}")
