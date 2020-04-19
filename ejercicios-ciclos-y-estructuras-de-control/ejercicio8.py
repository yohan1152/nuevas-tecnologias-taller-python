"""
    *listar todos los números pares del 0 al 100
"""
try:
    N = 100

    print("\nNúmeros pares del 0 al 100:\n")

    for i in range(N+1):
        if i%2 == 0:
            print(i)
except ValueError:
    print("\nError al procesar.")