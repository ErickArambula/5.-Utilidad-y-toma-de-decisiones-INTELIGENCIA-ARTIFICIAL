# Definición de estados y recompensas
estados = ["S", "A", "B", "C", "T"]  # S: Estado inicial, T: Estado terminal
recompensas = {"S": 0, "A": -1, "B": -1, "C": 10, "T": 0}

# Inicialización de una política inicial (arbitraria)
politica = {"S": "A", "A": "A", "B": "A", "C": "A", "T": None}

# Hiperparámetro de descuento
descuento = 0.9

# Algoritmo de iteración de políticas
for _ in range(100):
    for estado in estados:
        if estado not in ["S", "T"]:
            mejor_utilidad = recompensas[estado] + descuento * recompensas[politica[estado]]
            for accion in ["A", "B", "C"]:
                utilidad_accion = recompensas[estado] + descuento * recompensas[accion]
                if utilidad_accion > mejor_utilidad:
                    mejor_utilidad = utilidad_accion
                    politica[estado] = accion

# Mostrar la política óptima
for estado, accion in politica.items():
    print(f"En el estado {estado}, realizar la acción {accion}")
