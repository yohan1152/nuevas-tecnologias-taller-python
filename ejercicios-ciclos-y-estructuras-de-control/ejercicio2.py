"""
    *Crear una lista la cual almacene 10 números positivos ingresados
    por el usuario, mostrar en pantalla: la suma de todos los
    números, el promedio, el número mayor y el número menor.
"""

try:
    numeros = []
    N = 10
    suma = 0
    promedio = 0
    numMayor = 0
    numMenor = 0

    for i in range(N):
        numeros.append(float(input("Ingresar valor # %s:\n" %(i+1))))
        suma += numeros[i] 
    
    promedio = suma/len(numeros)
    numMayor = max(numeros)
    numMenor = min(numeros)
   
    print("\nSuma total: ", suma)
    print("\nPromedio: ", promedio)
    print("\nNúmero mayor: ", numMayor)
    print("\nNúmero menor: ", numMenor)

except ValueError:
    print("\nEl valor ingresado no es válido.")