class NodoDecision:
    def __init__(self, nombre):
        self.nombre = nombre
        self.opciones = []

    def agregar_opcion(self, opcion):
        self.opciones.append(opcion)

class Opcion:
    def __init__(self, nombre, probabilidad):
        self.nombre = nombre
        self.probabilidad = probabilidad
        self.resultado = None

    def agregar_resultado(self, resultado):
        self.resultado = resultado

class NodoResultado:
    def __init__(self, nombre, valor_utilidad):
        self.nombre = nombre
        self.valor_utilidad = valor_utilidad

# Creación de nodos de decisión y resultados
decision_compra = NodoDecision("Compra")
opcion_compra = Opcion("Comprar", 0.6)
opcion_no_compra = Opcion("No Comprar", 0.4)

decision_compra.agregar_opcion(opcion_compra)
decision_compra.agregar_opcion(opcion_no_compra)

resultado_bueno = NodoResultado("Resultado Bueno", 100)
resultado_malo = NodoResultado("Resultado Malo", 20)

opcion_compra.agregar_resultado(resultado_bueno)
opcion_no_compra.agregar_resultado(resultado_malo)

# Calcular el valor esperado
valor_esperado = opcion_compra.probabilidad * resultado_bueno.valor_utilidad + opcion_no_compra.probabilidad * resultado_malo.valor_utilidad

# Mostrar el valor esperado
print(f"El valor esperado de la decisión de compra es: {valor_esperado}")
