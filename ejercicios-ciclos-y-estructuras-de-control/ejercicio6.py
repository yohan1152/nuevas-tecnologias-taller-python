"""
    *Cantidad de vocales en una frase
    *Mostrar la frecuencia de aparición de vocales en una frase
"""
import unicodedata

def eliminar_acentos(frase):
    frase = frase.replace('ñ','#')
    res = ''.join((x for x in unicodedata.normalize('NFD',frase) if unicodedata.category(x) != 'Mn'))
    return res.replace('#','ñ')

try:
    frase = []
    a = ""
    e = ""
    i = ""
    o = ""
    u = ""

    frase = eliminar_acentos(input("Ingresar frase:\n").lower()) 

    a = frase.count("a")
    e = frase.count("e")
    i = frase.count("i")
    o = frase.count("o")
    u = frase.count("u")

    print("\nCantidad de la vocal 'a' en la frase:",a)
    print("Cantidad de la vocal 'e' en la frase:",e)
    print("Cantidad de la vocal 'i' en la frase:",i)
    print("Cantidad de la vocal 'o' en la frase:",o)
    print("Cantidad de la vocal 'u' en la frase:",u)
    print("\nTotal vocales en la frase:",(a+e+i+o+u))
except ValueError:
    print("\nEl valor ingresado no es válido.")