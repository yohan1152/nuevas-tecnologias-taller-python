"""
    *Dado una lista de frases ingresadas por el usuario, mostrar en
    pantalla todas aquellas que sean palíndromo.
"""
import unicodedata

def eliminar_acentos(frase):
       return ''.join(x for x in unicodedata.normalize('NFKD', frase) if unicodedata.category(x)[0] == 'L').lower()

try:
    palindromos = []
    fraseOriginal = ""
    N = 0
    aux = ""

    N = int(input("Cuántas frases desea ingresar?\n"))

    for i in range(N):
        fraseOriginal = input("Ingresar frase # %s:\n" %(i+1))
        aux = eliminar_acentos(fraseOriginal)
        if (aux == aux[::-1]): 
            palindromos.append(fraseOriginal)

    print("\nPalíndromos ingresados:")
    for i in range(len(palindromos)): 
            print("- ",palindromos[i])

except ValueError:
    print("\nEl valor ingresado no es válido.")