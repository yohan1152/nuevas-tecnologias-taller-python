"""
    5. Realice un algoritmo para generar e imprimir los números pares e impares que se encuentran
    entre 0 y 100. Además muestre la multiplicación de todos estos.
"""
try:
    N = 100
    impares = ""
    pares = ""
    multiplicacion = 1
    multiplicacionPar = 1
    multiplicacionImpar = 1
    #impares = []

    for i in range (N+1):
        multiplicacion *= i
        if i % 2 == 0:
            pares += str(i)+"\n"
            multiplicacionPar *= i
        else:
            impares += str(i)+"\n"
            multiplicacionImpar *= i
            
    print("\nNúmeros pares:\n", pares)
    print("\nNúmeros impares:\n", impares)
    #Como se toma el rango desde cero la multiplicación total y de los números pares da como resultado cero
    print("\nTotal multiplicación:\n",multiplicacion)
    print("\nTotal multiplicación Pares:\n",multiplicacionPar)
    print("\nTotal multiplicación Impares:\n{:,}".format(multiplicacionImpar).replace(',','.'))
except ValueError:
    print("Error.")