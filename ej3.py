#toma dos coordenadas x y y,
def spiral_number(x, y):
    #si x es mayor que y, se calcula el valor de la variable
    if x > y:
        return (x - 1) ** 2 + y 
    else:
        #si y es par, se calcula el valor de la variable
        if x % 2 == 0:
            return (y - 1) ** 2 + x
        #si y es impar, se calcula el valor de la variable
        else:
            return y ** 2 - x + 1
        
assert spiral_number(2, 2) == 3, "Error en el caso de prueba"
print("Prueba pasada exitosamente")

# (x - 1) ** 2 + y es el valor de la esquina superior derecha de la espiral
# (y - 1) ** 2 + x es el valor de la esquina inferior izquierda de la espiral
# y ** 2 - x + 1 es el valor de la esquina inferior derecha de la espiral