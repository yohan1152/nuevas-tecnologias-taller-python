"""
    2. Se requiere un algoritmo para obtener la suma de diez cantidades mediante la utilización de un
    ciclo for.
"""
try:
    N = 10
    suma = 0

    for i in range(N):
        suma += float(input("Ingresar valor # %s: \n" %(i+1)))

    print("\nSuma total: ", suma)
except ValueError:
    print("Error.")