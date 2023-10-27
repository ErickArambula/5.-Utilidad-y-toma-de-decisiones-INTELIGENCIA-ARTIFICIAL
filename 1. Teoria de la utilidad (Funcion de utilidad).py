# Definición de la función de utilidad
def funcion_utilidad(precio, calidad):
    # Esta es una función de utilidad simple que considera el precio y la calidad.
    # Puedes personalizar esta función según tus preferencias y necesidades.
    return calidad / precio

# Ejemplo de productos en una tienda en línea
producto_1 = {"nombre": "Laptop", "precio": 1000, "calidad": 8}
producto_2 = {"nombre": "Tablet", "precio": 500, "calidad": 7}
producto_3 = {"nombre": "Teléfono", "precio": 800, "calidad": 9}

# Calcular la utilidad para cada producto
utilidad_producto_1 = funcion_utilidad(producto_1["precio"], producto_1["calidad"])
utilidad_producto_2 = funcion_utilidad(producto_2["precio"], producto_2["calidad"])
utilidad_producto_3 = funcion_utilidad(producto_3["precio"], producto_3["calidad"])

# Comparar productos basados en su utilidad
if utilidad_producto_1 > utilidad_producto_2 and utilidad_producto_1 > utilidad_producto_3:
    mejor_producto = producto_1["nombre"]
elif utilidad_producto_2 > utilidad_producto_1 and utilidad_producto_2 > utilidad_producto_3:
    mejor_producto = producto_2["nombre"]
else:
    mejor_producto = producto_3["nombre"]

# Mostrar el mejor producto basado en la utilidad
print(f"El mejor producto es: {mejor_producto}")
