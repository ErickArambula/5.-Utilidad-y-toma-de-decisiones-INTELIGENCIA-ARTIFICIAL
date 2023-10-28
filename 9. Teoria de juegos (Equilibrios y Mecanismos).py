from nashpy import Game

# Matriz de pagos del jugador 1 (fila) y jugador 2 (columna)
jugador1 = [[3, 0], [5, 1]]
jugador2 = [[3, 5], [0, 1]]

# Crear el juego
juego = Game(jugador1, jugador2)

# Encontrar el equilibrio de Nash en estrategias mixtas
equilibrio = juego.support_enumeration()

# Mostrar el resultado
for estrategia in equilibrio:
    print(f"Jugador 1: {estrategia[0]}, Jugador 2: {estrategia[1]}")
