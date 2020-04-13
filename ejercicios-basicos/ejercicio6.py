"""
    6. Realice un algoritmo para generar N elementos de la sucesión de Fibonacci (0, 1, 1, 2, 3, 5, 8,
    13,…).
"""

try:
    N = 0
    aux = 0
    inicio = 0 
    siguiente = 1
    serieFibonacci = "0"

    N = int(input("Ingresar el número de iteraciones para la serie de Fibonacci:\n"))

    for i in range (N):
        serieFibonacci += ", "+str(siguiente) 
        aux = inicio + siguiente
        inicio = siguiente
        siguiente = aux
        
    print ("\nSerie de Fibonacci: ",serieFibonacci)

except ValueError:
    print("Valor ingresado no válido.")