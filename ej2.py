def missing_number(n, arr):
    # Se crea una lista para almacenar los números que faltan
    faltan = []
    # Se recorre de 1 a n
    for i in range(1, n+1):
        # Si el nro no está en la lista, se agrega a la lista de faltantes
        if i not in arr:
            faltan.append(i)
        # Si la lista de faltantes tiene la misma cantidad de elementos que la lista de entrada, se retorna la lista de faltantes
    return faltan

# Prueba de la función con un caso de ejemplo
assert missing_number(5, [1, 2, 4, 6]) == [3, 5], "Error en el caso de prueba"
print("Prueba pasada exitosamente")
#append agrega un elemento al final de la lista

