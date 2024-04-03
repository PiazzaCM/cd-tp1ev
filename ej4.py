def palindrome_reorder(letras):
    # inicializamos una lista vacía para almacenar las cantidaades de cada letra
    conteo = {}
    # Recorremos la lista de letras
    for i in letras:
        for letra in i:
            # Si la letra esta en la lista, aumentamos su cuenta en 1
            if letra in conteo:
                conteo[letra] += 1
            # Si la letra no esta, la inicializamos con 1
            else:
                conteo[letra] = 1

    # Contamos las letras que son impares
    impares = sum(1 for count in conteo.values() if count % 2 != 0)
    # Si hay más de una letra con una cantidad impar, retornamos "NO SOLUTION"
    if impares > 1:
        return "NO SOLUTION"

    palindromo = ""

    # Primero agregamos las letras pares
    for letra, count in conteo.items():
        if count % 2 == 0:
            # Agregamos la mitad de las letras
            palindromo += letra * (count // 2)

    # Luego agregamos la letra impar, si existe
    letra_impar = ""
    for letra, count in conteo.items(): # Buscamos la letra impar
        if count % 2 != 0: 
            letra_impar = letra
            break

    palabra = palindromo + letra_impar + palindromo[::-1] # Agregamos la letra impar y la mitad de las letras en orden inverso

    return palabra


# Ejemplo de assertions
assert palindrome_reorder(["aabbc"]) == "abcba", "Error en el caso de prueba"
print("Prueba pasada exitosamente")
