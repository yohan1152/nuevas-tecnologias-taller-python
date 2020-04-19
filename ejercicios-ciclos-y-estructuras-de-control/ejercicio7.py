"""
    *Eliminar vocales de una frase
"""
import unicodedata

def eliminar_acentos(frase):
    frase = frase.replace('ñ','#')
    res = ''.join((x for x in unicodedata.normalize('NFD',frase) if unicodedata.category(x) != 'Mn'))
    return res.replace('#','ñ')

try:
    fraseOriginal = ""
    frase = ""

    fraseOriginal = eliminar_acentos(input("Ingresar frase:\n").lower())
    frase = fraseOriginal.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')

    print("\nFrase sin vocales:",frase)
except ValueError:
    print("\nEl valor ingresado no es válido.")