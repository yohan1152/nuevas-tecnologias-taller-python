"""
    3. Se requiere un algoritmo para obtener la estatura promedio de un grupo de personas, cuyo
    número de miembros se desconoce, el ciclo debe efectuarse siempre y cuando se tenga una
    estatura registrada.
"""
try:
    estatura = -1
    sumarEstatura = 0
    contarEstatura = 0

    while estatura:
        estatura = float(input("Ingresar estatura:\n")) 
        sumarEstatura += estatura
        contarEstatura += 1
        #El enunciado no especificaba en que momento de debia mostrar el promedio por eso lo muestro en cada iteración
        print("\nEstatura promedio: ", sumarEstatura/contarEstatura,"\n")
except ValueError:
    print("El valor ingeresado no es un número válido.")
    print("\nEstatura promedio: ", sumarEstatura/contarEstatura)
