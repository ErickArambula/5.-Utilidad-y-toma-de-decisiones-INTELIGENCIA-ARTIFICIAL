import numpy as np

# Definición de estados, acciones y recompensas
estados = [0, 1, 2]  # Estados: 0 - Cara, 1 - Sello, 2 - Fin
acciones = [0, 1]    # Acciones: 0 - Elegir Cara, 1 - Elegir Sello

# Matriz de transición del estado
P = np.array([[[0.5, 0.5, 0.0],  # Desde estado 0 (Cara)
              [0.0, 0.0, 1.0]],  # Desde estado 1 (Sello)
             [[1.0, 0.0, 0.0],  # Desde estado 0 (Cara)
              [0.0, 1.0, 0.0]]])  # Desde estado 1 (Sello)

# Matriz de recompensas
R = np.array([[1, -1, 0],  # Recompensas al elegir Cara
              [0, -1, 0]])  # Recompensas al elegir Sello

# Hiperparámetro de descuento
descuento = 0.9

# Inicialización de los valores óptimos
valores_optimos = np.zeros(len(estados))

# Algoritmo de iteración de políticas
epsilon = 1e-6
while True:
    delta = 0
    for estado in estados:
        v = valores_optimos[estado]
        nueva_valor = np.max(np.sum(P[:, estado, :] * (R[:, estado] + descuento * valores_optimos), axis=1))
        valores_optimos[estado] = nueva_valor
        delta = max(delta, abs(v - nueva_valor))
    if delta < epsilon:
        break

# Política óptima
politica_optima = np.argmax(np.sum(P * (R + descuento * valores_optimos), axis=2), axis=1)

# Mostrar la política óptima
print("Política óptima:", politica_optima)

# Mostrar los valores óptimos
print("Valores óptimos:", valores_optimos)
