def weird_algorithm(n):
    # Se crea una lista para almacenar los números de la secuencia
    secuencia = []
    # Se verifica que el número ingresado sea positivo
    while n != 1:
        secuencia.append(n)
        # Si el número es par, se divide por 2
        if n % 2 == 0:
            n = n // 2
        # Si el número es impar, se multiplica por 3 y se suma 1
        else:
            n = n * 3 + 1
    secuencia.append(n) 
    return secuencia

# Prueba de la función con un caso de ejemplo
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
print("Prueba pasada exitosamente")