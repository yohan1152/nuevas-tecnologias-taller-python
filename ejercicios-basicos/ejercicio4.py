"""
    4. Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores o iguales a
    cero y cuántas mayores a cero.
"""
try:
    N = 0
    valor = 0
    contarMayorCero = 0
    contarMenorIgualCero = 0

    N = int(input("Ingresar número de iteraciones:\n"))

    for i in range(N):
        valor = float(input("Ingresar valor # %s:\n" %(i+1))) 
        if valor > 0: 
            contarMayorCero += 1 
        else:
            contarMenorIgualCero += 1 
    
    print("\nTotal mayor a cero: ", contarMayorCero,"\nTotal menor o igual a cero:",contarMenorIgualCero)
except ValueError:
    print("El valor ingeresado no es un número válido.")
    print("\nTotal mayor a cero: ", contarMayorCero,"\nTotal menor o igual a cero:",contarMenorIgualCero)