"""
    *Dado una lista de frases ingresadas por el usuario, mostrar en
    pantalla todas aquellas que sean palíndromo.
"""
try:
    frases = []
    N = 0

    N = int(input("Cuántas frases desea ingresar?\n"))

    for i in range(N):
        frases.append(input("Ingresar frase # %s:\n" %(i+1)))
        if numeros[i] == reverse(numeros[i]): 
            print("\n",numeros[i])

except ValueError:
    print("\nEl valor ingresado no es válido.")